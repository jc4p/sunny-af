import requests
import json
import random

from pprint import pprint
from secrets import *

from collections import defaultdict
from deco import concurrent, synchronized

import datetime
import dateutil.relativedelta as relativedelta

DESTINATIONS = [
    {"name": "Pensacola", "code": "PNS"},
    {"name": "Myrtle Beach", "code": "MYR"},
    {"name": "Tybee Island", "code": "SAV"},
    {"name": "Virginia Beach", "code": "ORF"},
    {"name": "Carolina Beach", "code": "OAJ"},
    {"name": "Laguna Beach", "code": "SNA"},
    {"name": "Puerto Rico", "code": "SJU"},
    {"name": "Boca Raton", "code": "FLL"},
    {"name": "Folly Beach", "code": "CHS"}
]

def make_search_payload(from_code, to_code, date_start, date_end, nonstop=False):
    return {
      "request": {
        "passengers": {
          "kind": "qpxexpress#passengerCounts",
          "adultCount": 1,
          "childCount": 0,
          "infantInLapCount": 0,
          "infantInSeatCount": 0,
          "seniorCount": 0
        },
        "slice": [
          {
            "kind": "qpxexpress#sliceInput",
            "origin": from_code,
            "destination": to_code,
            "date": date_start,
            "maxStops": 0 if nonstop else 3
          },
          {
            "kind": "qpxexpress#sliceInput",
            "origin": to_code,
            "destination": from_code,
            "date": date_end,
            "maxStops": 0 if nonstop else 3
          }
        ],
        "solutions": 3
      }
    }


@concurrent
def get_trips(from_code, to_code, date_start, date_end, nonstop):
    page = requests.post("https://www.googleapis.com/qpxExpress/v1/trips/search",
                params={"key": GOOGLE_API_KEY},
                json=make_search_payload(from_code, to_code, date_start, date_end, nonstop))
    if page.status_code != 200:
        print page.content
        return None
    res = page.json()

    if "trips" not in res:
        return None
    if "tripOption" not in res['trips'] or "data" not in res['trips']:
        return None

    return res["trips"]["tripOption"]

@synchronized
def get_possible_trips(from_code, to_code, depart_date, arrival_date, nonstop):
  results = defaultdict(dict)
  for depart_delta in [-1, 0, 1]:
    depart_date_str = str(depart_date + relativedelta.relativedelta(days=depart_delta))
    for arrival_delta in [-1, 0, 1]:
      arrival_date_str = str(arrival_date + relativedelta.relativedelta(days=arrival_delta))
      results[depart_date_str][arrival_date_str] = get_trips(from_code, to_code,
          depart_date_str, arrival_date_str, nonstop)
  return dict(results)


# TODO: Use a redis based local flight cache, based on the code for https://github.com/jc4p/lol-data-analysis
if __name__ == "__main__":
    destination = random.choice(DESTINATIONS)
    today = datetime.date.today()
    # Let's look for flights -1/+1 days from next-next Friday
    depart_date = today + relativedelta.relativedelta(days=7, weekday=relativedelta.FR)
    # And arriving -1/+1 days from the next Monday
    arrival_date = depart_date + relativedelta.relativedelta(days=3)

    trips = get_possible_trips("DEN", destination['code'], depart_date, arrival_date, False)
    print "Trips between DEN and {}".format(destination['code'])
    for depart_delta in [-1, 0, 1]:
      depart_date_str = str(depart_date + relativedelta.relativedelta(days=depart_delta))
      for arrival_delta in [-1, 0, 1]:
        arrival_date_str = str(arrival_date + relativedelta.relativedelta(days=arrival_delta))
        if trips[depart_date_str][arrival_date_str]:
          for trip in trips[depart_date_str][arrival_date_str]:
            print "{} -> {}".format(depart_date_str, arrival_date_str)
            line = trip['saleTotal'] + " \t"
            for s in trip['slice']:
                line += "{} {} {} to {} ".format(s['segment'][0]['flight']['carrier'],
                    s['segment'][0]['flight']['number'], s['segment'][0]['leg'][0]['origin'],
                    s['segment'][0]['leg'][0]['destination'])
            print line
          print ""