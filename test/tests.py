import json
import unittest

from nose.tools import eq_
from models import *
from data import *

class TripOptionTest(unittest.TestCase):
  def setUp(self):
    full_json = json.loads(DEN_NYC_ROUNDTRIP_2017_04_01)
    first_option = full_json['trips']['tripOption'][0]

    self.trip_option = TripOption(first_option)

  def test_process_sale_total(self):
    eq_(self.trip_option.price, 369.40)
    eq_(self.trip_option.price_currency, 'USD')

  def test_basic_info(self):
    eq_(self.trip_option.origin, 'DEN')
    eq_(self.trip_option.destination, 'JFK')
    eq_(self.trip_option.roundtrip, True)
    eq_(self.trip_option.total_mileage, 3240)
