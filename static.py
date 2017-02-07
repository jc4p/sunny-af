DESTINATIONS = [
  {"name": "Pensacola, FL", "code": "PNS"},
  {"name": "Myrtle Beach, SC", "code": "MYR"},
  {"name": "Tybee Island, GA", "code": "SAV"},
  {"name": "Virginia Beach, VA", "code": "ORF"},
  {"name": "Carolina Beach, NC", "code": "OAJ"},
  {"name": "Laguna Beach, CA", "code": "SNA"},
  {"name": "San Juan, PR", "code": "SJU"},
  {"name": "Boca Raton, FL", "code": "FLL"},
  {"name": "Folly Beach, SC", "code": "CHS"},
  {"name": "Long Beach, WA", "code": "PDX"},
  {"name": "Clearwater, WA", "code": "TPA"},
  {"name": "San Diego, CA", "code": "SAN"},
  {"name": "Maui, HI", "code": "OGG"},
  {"name": "Provincetown, MA", "code": "PVC"},
  {"name": "Carmel-by-the-Sea, CA", "code": "MRY"}
]

ORIGINS = [
  {"name": "New York, NY", "code": "NYC"},
  {"name": "Denver, CO", "code": "DEN"},
  {"name": "San Francisco, CA", "code": "SFO"}
]

DARK_SKY_ROUTE = 'https://api.darksky.net/forecast/{api_key}/{latitude:.4f},{longitude:.4f},{time}'

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
          "date": date_start.strftime("%Y-%m-%d"),
          "maxStops": 0 if nonstop else 1
        },
        {
          "kind": "qpxexpress#sliceInput",
          "origin": to_code,
          "destination": from_code,
          "date": date_end.strftime("%Y-%m-%d"),
          "maxStops": 0 if nonstop else 1
        }
      ],
      "solutions": 3
    }
  }
