import requests
import json
import random

from pprint import pprint

from secrets import *
from models import *

from collections import defaultdict
from multiprocessing import Pool, Process

import datetime
import dateutil.relativedelta as relativedelta


def get_trips(from_code, to_code, date_start, date_end, nonstop):
    page = requests.post("https://www.googleapis.com/qpxExpress/v1/trips/search",
                params={"key": GOOGLE_API_KEY},
                json=make_search_payload(from_code, to_code, date_start, date_end, nonstop))
    if page.status_code != 200:
        print(page.content)
        return None
    res = page.json()

    if "trips" not in res:
        return None
    if "tripOption" not in res['trips'] or "data" not in res['trips']:
        return None

    return [TripOption(x) for x in res['trips']['tripOption']]

def get_possible_trips(from_code, to_code, depart_date, arrival_date, nonstop):
  args = []
  for depart_delta in [-1, 0, 1]:
    depart_date_str = str(depart_date + relativedelta.relativedelta(days=depart_delta))

    for arrival_delta in [-1, 0, 1]:
      arrival_date_str = str(arrival_date + relativedelta.relativedelta(days=arrival_delta))
      args.append((from_code, to_code, depart_date_str, arrival_date_str, nonstop))

  with Pool(3) as pool:
    return pool.starmap(get_trips, args)

# TODO: Use a redis based local flight cache, based on the code for https://github.com/jc4p/lol-data-analysis
if __name__ == "__main__":
    destination = random.choice(DESTINATIONS)
    today = datetime.utcnow().date()
    # Let's look for flights -1/+1 days from next-next Friday
    depart_date = today + relativedelta.relativedelta(days=7, weekday=relativedelta.FR)
    # And arriving -1/+1 days from the next Monday
    arrival_date = depart_date + relativedelta.relativedelta(days=3)

    trips = get_possible_trips("DEN", destination['code'], depart_date, arrival_date, False)
    print(trips)

    # print("Trips between DEN and {}".format(destination['code']))
    # for depart_delta in [-1, 0, 1]:
    #   depart_date_str = str(depart_date + relativedelta.relativedelta(days=depart_delta))

    #   for arrival_delta in [-1, 0, 1]:
    #     arrival_date_str = str(arrival_date + relativedelta.relativedelta(days=arrival_delta))

    #     if trips[depart_date_str][arrival_date_str]:
    #       for trip in trips[depart_date_str][arrival_date_str]:
    #         print("{} -> {}".format(depart_date_str, arrival_date_str))
    #         line = trip['saleTotal'] + " \t"
    #         for s in trip['slice']:
    #             line += "{} {} {} to {} ".format(s['segment'][0]['flight']['carrier'],
    #                 s['segment'][0]['flight']['number'], s['segment'][0]['leg'][0]['origin'],
    #                 s['segment'][0]['leg'][0]['destination'])
    #         print(line)
    #       print("")