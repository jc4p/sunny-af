import dateutil.parser

class TripOption:
  """Wrapper around Google QPX's TripInfo object"""
  def __init__(self, json):
    self.price, self.price_currency = self.process_sale_total(json['saleTotal'])
    self.slices = []

    for s in json['slice']:
      self.slices.append(TripOptionSlice(s))

    # Quick way to access the first slice of the flight (typically, first half of a roundtrip)
    first_segment = self.slices[0].segments[0]
    last_segment = self.slices[0].segments[-1]

    self.origin = first_segment.legs[0].origin
    self.destination = last_segment.legs[-1].destination

    self.origin_departure = first_segment.legs[0].departureTime
    # Note that this is slices[-1], not slices[0], because if it's a roundtrip
    # we want to capture when we come back home, not when we land at destination.
    # If it's not a roundtrip, slices[-1] will be slices[0] so no worries.
    self.origin_arrival = self.slices[-1].segments[-1].legs[-1].arrivalTime
    
    self.roundtrip = len(self.slices) > 1
    self.total_mileage = 0
    
    for s in self.slices:
      for seg in s.segments:
        for leg in seg.legs:
          self.total_mileage += leg.mileage


  def process_sale_total(self, s):
    first_digit = -1

    for i in range(len(s)):
      if s[i].isdigit():
        first_digit = i
        break
    if first_digit == -1:
      return None, None

    currency = s[0:i]
    price = float(s[i:])

    return price, currency

  def __repr__(self):
    return "<Trip {}-{} {:%m/%d}-{:%m/%d} ${}>".format(self.origin, self.destination,
        self.origin_departure, self.origin_arrival, self.price)


class TripOptionSlice:
  def __init__(self, json):
    self.duration = json['duration']
    self.segments = []

    for segment in json['segment']:
      self.segments.append(TripOptionSegment(segment))

  def __repr__(self):
    segments_str = ["{} {}".format(x.airline, x.number) for x in self.segments]
    return "<Slice {}>".format(",".join(segments_str))


class TripOptionSegment:
  def __init__(self, s):
    self.airline = s['flight']['carrier']
    self.number = s['flight']['number']
    self.cabin = s['cabin']
    self.legs = []

    for leg in s['leg']:
      self.legs.append(TripOptionSegmentLeg(leg))

  def __repr__(self):
    return "<Segment {} {}>".format(self.airline, self.number)


class TripOptionSegmentLeg:
  def __init__(self, s):
    self.aircraft = s['aircraft']
    self.arrivalTime = dateutil.parser.parse(s['arrivalTime'])
    self.departureTime = dateutil.parser.parse(s['departureTime'])
    
    self.origin = s['origin']
    self.destination = s['destination']
    
    self.mileage = s['mileage']

  def __repr__(self):
    return "<Leg {} to {}>".format(self.origin, self.destination)




