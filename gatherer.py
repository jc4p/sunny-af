from models import *
from static import *
from secrets import *

from datetime import datetime
from dateutil import relativedelta
from geopy.geocoders import GoogleV3
from multiprocessing import Pool

import requests
import redis
import pickle
import itertools

redis = redis.StrictRedis(host='localhost', port=6379, db=0)

cached_trips = [str(x, 'UTF-8') for x in redis.hkeys('trips')]
cached_geos = [str(x, 'UTF-8') for x in redis.hkeys('geocodes')]
cached_weather = [str(x, 'UTF-8') for x in redis.hkeys('weather')]
cached_trip_weather = [str(x, 'UTF-8') for x in redis.hkeys('trip_weather')]

def get_trips(from_code, to_code, date_start, date_end, nonstop):
  page = requests.post("https://www.googleapis.com/qpxExpress/v1/trips/search",
              params={"key": GOOGLE_API_KEY},
              json=make_search_payload(from_code, to_code, date_start, date_end, nonstop))
  if page.status_code != 200:
      print(page.content)
      raise ValueError("Rate Limited, I think")
      return []
  res = page.json()

  if "trips" not in res:
      return []
  if "tripOption" not in res['trips'] or "data" not in res['trips']:
      return []

  return [TripOption(x) for x in res['trips']['tripOption']]

def get_possible_trips(from_code, to_code, depart_date, arrival_date):
  cache_key = '{}_{}_{:%y_%m_%d}_{:%y_%m_%d}'.format(from_code, to_code, depart_date, arrival_date)
  if cache_key in cached_trips:
    return pickle.loads(redis.hget('trips', cache_key))
  args = []
  for depart_delta in [-1, 0, 1]:
    depart_date_incr = depart_date + relativedelta.relativedelta(days=depart_delta)

    for arrival_delta in [-1, 0, 1]:
      arrival_date_incr = arrival_date + relativedelta.relativedelta(days=arrival_delta)
      args.append((from_code, to_code, depart_date_incr, arrival_date_incr, True))

  with Pool(5) as pool:
    trips = pool.starmap(get_trips, args)
    redis.hset('trips', cache_key, pickle.dumps(trips))
    return trips

def get_geocode(query, geocoder=None):
  location = geocoder.geocode(query)
  return (location.latitude, location.longitude)

def get_query_geo(query, geocoder=None):
  cache_key = '{}'.format(query['code'])
  if cache_key in cached_geos:
    latitude, longitude = pickle.loads(redis.hget('geocodes', cache_key))
    return (latitude, longitude)
  else:
    latitude, longitude = get_geocode(query['name'], geocoder=geocoder)
    redis.hset('geocodes', cache_key, pickle.dumps((latitude, longitude)))
    return (latitude, longitude)


def get_weather(latitude, longitude, start_date, end_date, destination):
  cache_key = '{:.4f}_{:.4f}_{:%y_%m_%d}_{:%y_%m_%d}'.format(latitude, longitude, start_date, end_date)
  if cache_key in cached_weather:
    return pickle.loads(redis.hget('weather', cache_key))
  for day_index in range((end_date-start_date).days):
    midday = start_date + relativedelta.relativedelta(days=day_index, hours=12)

    uri = DARK_SKY_ROUTE.format(api_key=DARK_SKY_API_KEY, latitude=latitude,
                                longitude=longitude, time=int(midday.timestamp()))
    page = requests.get(uri)
    if page.status_code != 200:
        print(page.content)
        return None
    data = page.json()['daily']['data'][0]
    report = WeatherReport(data, midday, destination['name'], destination['code'])
    redis.hset('weather', cache_key, pickle.dumps(report))
    return report


def prepare_trip_weather_reports(geocoder):
  if cached_trip_weather:
    return
  for city in DESTINATIONS:
    airport_code = city['code']
    latitude, longitude = get_query_geo(city, geocoder=geocoder)

    for week_index in range(1, 3):
      today = datetime.utcnow().date()
      depart_date = today + relativedelta.relativedelta(days=7 * week_index, weekday=relativedelta.FR)
      arrival_date = depart_date + relativedelta.relativedelta(days=3)

      cache_key = '{}_{:%y_%m_%d}'.format(city['code'], depart_date)
      if cache_key in cached_trip_weather:
        continue

      args = []

      for depart_delta in [-1, 0, 1]:
        depart_date_inc = (depart_date + relativedelta.relativedelta(days=depart_delta))

      for arrival_delta in [-1, 0, 1]:
        arrival_date_inc = arrival_date + relativedelta.relativedelta(days=arrival_delta)
        args.append((latitude, longitude, depart_date_inc, arrival_date_inc, city))

    with Pool(5) as pool:
      reports = pool.starmap(get_weather, args)
      redis.hset('trip_weather', cache_key, pickle.dumps(reports))

if __name__ == "__main__":
  geocoder = GoogleV3(api_key=GOOGLE_MAPS_GEOCODING_API_KEY)

  prepare_trip_weather_reports(geocoder)

  keys = [str(x, 'UTF-8') for x in redis.hkeys('trip_weather')]
  forecasts = []
  for key in keys:
    forecasts += pickle.loads(redis.hget('trip_weather', key))
  forecasts = list(set(forecasts))
  #fridays = [x for x in forecasts if x.date.date().weekday() == 4]
  clear_skies = [x for x in forecasts if x.precipProbability == 0.0 or x.precipType == '']
  warm = [x for x in clear_skies if x.temperatureMax > 68]

  trips = []
  for possible in warm:
    for city in ORIGINS:
      start = possible.date
      end = start + relativedelta.relativedelta(days=3)
      res = get_possible_trips(city['code'], possible.airport_code, start, end)
      trips.append(list(itertools.chain.from_iterable(res)))

  for t in trips:
    if len(t) < 1 or not t[0]:
      continue
    origin = t[0].origin
    destination = t[0].destination
    destination_name = [x['name'] for x in DESTINATIONS if x['code'] == destination][0]

    cheap = [x for x in t if x and x.price < 300.0]
    cheap = sorted(cheap, key=lambda x: x.price)
    if len(cheap) > 2:
      cheap = cheap[0:2]
    for c in cheap:
      weather_report = [x for x in warm if x.airport_code == c.destination]
      summary = ''
      if weather_report:
        report = weather_report[0]
        summary = '{:.0f}F/{:.0f}F, {}'.format(report.temperatureMin, report.temperatureMax, report.summary)

      print("{} to {}".format(origin, destination_name))
      print("${:.2f}  {:%A %y-%m-%d %I:%M%p} - {:%A %y-%m-%d %I:%M%p}\n  {}".format(
        c.price, c.origin_departure, c.origin_arrival, summary))

