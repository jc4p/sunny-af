DEN_NYC_ROUNDTRIP_2017_04_01 = """
{
 "kind": "qpxExpress#tripsSearch",
 "trips": {
  "kind": "qpxexpress#tripOptions",
  "requestId": "uXpFumaL1f5M6OfPm0PwoO",
  "data": {
   "kind": "qpxexpress#data",
   "airport": [
    {
     "kind": "qpxexpress#airportData",
     "code": "DEN",
     "city": "DEN",
     "name": "Denver International"
    },
    {
     "kind": "qpxexpress#airportData",
     "code": "EWR",
     "city": "EWR",
     "name": "Newark Liberty International"
    },
    {
     "kind": "qpxexpress#airportData",
     "code": "JFK",
     "city": "NYC",
     "name": "New York John F Kennedy International"
    }
   ],
   "city": [
    {
     "kind": "qpxexpress#cityData",
     "code": "DEN",
     "name": "Denver"
    },
    {
     "kind": "qpxexpress#cityData",
     "code": "EWR",
     "name": "Newark"
    },
    {
     "kind": "qpxexpress#cityData",
     "code": "NYC",
     "name": "New York"
    }
   ],
   "aircraft": [
    {
     "kind": "qpxexpress#aircraftData",
     "code": "321",
     "name": "Airbus A321"
    },
    {
     "kind": "qpxexpress#aircraftData",
     "code": "738",
     "name": "Boeing 737"
    },
    {
     "kind": "qpxexpress#aircraftData",
     "code": "739",
     "name": "Boeing 737"
    },
    {
     "kind": "qpxexpress#aircraftData",
     "code": "777",
     "name": "Boeing 777"
    }
   ],
   "tax": [
    {
     "kind": "qpxexpress#taxData",
     "id": "ZP",
     "name": "US Flight Segment Tax"
    },
    {
     "kind": "qpxexpress#taxData",
     "id": "AY_001",
     "name": "US September 11th Security Fee"
    },
    {
     "kind": "qpxexpress#taxData",
     "id": "US_001",
     "name": "US Transportation Tax"
    },
    {
     "kind": "qpxexpress#taxData",
     "id": "XF",
     "name": "US Passenger Facility Charge"
    }
   ],
   "carrier": [
    {
     "kind": "qpxexpress#carrierData",
     "code": "B6",
     "name": "Jetblue Airways Corporation"
    },
    {
     "kind": "qpxexpress#carrierData",
     "code": "UA",
     "name": "United Airlines, Inc."
    }
   ]
  },
  "tripOption": [
   {
    "kind": "qpxexpress#tripOption",
    "saleTotal": "USD369.40",
    "id": "3K4245DYagKMD7ZY8rl7iP001",
    "slice": [
     {
      "kind": "qpxexpress#sliceInfo",
      "duration": 222,
      "segment": [
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 222,
        "flight": {
         "carrier": "B6",
         "number": "98"
        },
        "id": "G5Tu8XLVW7egN7ty",
        "cabin": "COACH",
        "bookingCode": "U",
        "bookingCodeCount": 4,
        "marriedSegmentGroup": "0",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "LKeylj7NGITugtrt",
          "aircraft": "321",
          "arrivalTime": "2017-04-02T05:40-04:00",
          "departureTime": "2017-04-01T23:58-06:00",
          "origin": "DEN",
          "destination": "JFK",
          "destinationTerminal": "5",
          "duration": 222,
          "onTimePerformance": 40,
          "mileage": 1620,
          "secure": true
         }
        ]
       }
      ]
     },
     {
      "kind": "qpxexpress#sliceInfo",
      "duration": 288,
      "segment": [
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 288,
        "flight": {
         "carrier": "B6",
         "number": "97"
        },
        "id": "GfqJfcJubet6Cpw-",
        "cabin": "COACH",
        "bookingCode": "M",
        "bookingCodeCount": 7,
        "marriedSegmentGroup": "1",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "LXLbjvtGQVgLahvy",
          "aircraft": "321",
          "arrivalTime": "2017-04-08T22:48-06:00",
          "departureTime": "2017-04-08T20:00-04:00",
          "origin": "JFK",
          "destination": "DEN",
          "originTerminal": "5",
          "duration": 288,
          "onTimePerformance": 60,
          "mileage": 1620,
          "secure": true
         }
        ]
       }
      ]
     }
    ],
    "pricing": [
     {
      "kind": "qpxexpress#pricingInfo",
      "fare": [
       {
        "kind": "qpxexpress#fareInfo",
        "id": "Awlj33D+kZS6L0Yq6qUpTmEo6ZRW8m+VCiUaalLt4MRaBDSLUkNGIi93KGrQhFETr22eoYTfWbsuL0R1Gwxt0BEXK5CLNk+pcQ5cChbKD8wOpotBrxFlmDwqZNVVCkntT6/c6sZpEjBCYD/",
        "carrier": "B6",
        "origin": "DEN",
        "destination": "NYC",
        "basisCode": "UI2ABEN5",
        "private": true
       },
       {
        "kind": "qpxexpress#fareInfo",
        "id": "AmHD3I2yrusPpAB3rsdNpDLPYzx4Qcxis+BWphQ/2xZTJVXqm6TFqV2HCDJCjDu8YZ6MY11ZzJ5glLIL4Jrm3lMPOEwELzZXkK3Se01Wfe6ykZyZUw5NNtHFhh9xwU+DaSD2tMS6pW554LU",
        "carrier": "B6",
        "origin": "NYC",
        "destination": "DEN",
        "basisCode": "MH4QBEN5",
        "private": true
       }
      ],
      "segmentPricing": [
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "Awlj33D+kZS6L0Yq6qUpTmEo6ZRW8m+VCiUaalLt4MRaBDSLUkNGIi93KGrQhFETr22eoYTfWbsuL0R1Gwxt0BEXK5CLNk+pcQ5cChbKD8wOpotBrxFlmDwqZNVVCkntT6/c6sZpEjBCYD/",
        "segmentId": "G5Tu8XLVW7egN7ty"
       },
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "AmHD3I2yrusPpAB3rsdNpDLPYzx4Qcxis+BWphQ/2xZTJVXqm6TFqV2HCDJCjDu8YZ6MY11ZzJ5glLIL4Jrm3lMPOEwELzZXkK3Se01Wfe6ykZyZUw5NNtHFhh9xwU+DaSD2tMS6pW554LU",
        "segmentId": "GfqJfcJubet6Cpw-"
       }
      ],
      "baseFareTotal": "USD317.21",
      "saleFareTotal": "USD317.21",
      "saleTaxTotal": "USD52.19",
      "saleTotal": "USD369.40",
      "passengers": {
       "kind": "qpxexpress#passengerCounts",
       "adultCount": 1
      },
      "tax": [
       {
        "kind": "qpxexpress#taxInfo",
        "id": "US_001",
        "chargeType": "GOVERNMENT",
        "code": "US",
        "country": "US",
        "salePrice": "USD23.79"
       },
       {
        "kind": "qpxexpress#taxInfo",
        "id": "AY_001",
        "chargeType": "GOVERNMENT",
        "code": "AY",
        "country": "US",
        "salePrice": "USD11.20"
       },
       {
        "kind": "qpxexpress#taxInfo",
        "id": "XF",
        "chargeType": "GOVERNMENT",
        "code": "XF",
        "country": "US",
        "salePrice": "USD9.00"
       },
       {
        "kind": "qpxexpress#taxInfo",
        "id": "ZP",
        "chargeType": "GOVERNMENT",
        "code": "ZP",
        "country": "US",
        "salePrice": "USD8.20"
       }
      ],
      "fareCalculation": "DEN B6 NYC 132.09UI2ABEN5 B6 DEN 185.12MH4QBEN5 USD 317.21 END ZP DEN JFK XT 23.79US 8.20ZP 11.20AY 9.00XF DEN4.50 JFK4.50",
      "latestTicketingTime": "2017-02-06T23:59-05:00",
      "ptc": "ADT"
     }
    ]
   },
   {
    "kind": "qpxexpress#tripOption",
    "saleTotal": "USD456.40",
    "id": "3K4245DYagKMD7ZY8rl7iP003",
    "slice": [
     {
      "kind": "qpxexpress#sliceInfo",
      "duration": 225,
      "segment": [
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 225,
        "flight": {
         "carrier": "UA",
         "number": "331"
        },
        "id": "Ga+MVN5CvJaw6vwj",
        "cabin": "COACH",
        "bookingCode": "K",
        "bookingCodeCount": 9,
        "marriedSegmentGroup": "0",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "L7t+eMyk-Q8zz+jv",
          "aircraft": "738",
          "arrivalTime": "2017-04-01T21:25-04:00",
          "departureTime": "2017-04-01T15:40-06:00",
          "origin": "DEN",
          "destination": "EWR",
          "destinationTerminal": "C",
          "duration": 225,
          "onTimePerformance": 60,
          "mileage": 1600,
          "meal": "Food for Purchase",
          "secure": true
         }
        ]
       }
      ]
     },
     {
      "kind": "qpxexpress#sliceInfo",
      "duration": 264,
      "segment": [
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 264,
        "flight": {
         "carrier": "UA",
         "number": "1961"
        },
        "id": "Ggukoy1Wdj8JYSnL",
        "cabin": "COACH",
        "bookingCode": "W",
        "bookingCodeCount": 9,
        "marriedSegmentGroup": "1",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "LdF-m5MFCtnO7Usc",
          "aircraft": "739",
          "arrivalTime": "2017-04-08T20:29-06:00",
          "departureTime": "2017-04-08T18:05-04:00",
          "origin": "EWR",
          "destination": "DEN",
          "originTerminal": "C",
          "duration": 264,
          "onTimePerformance": 80,
          "mileage": 1600,
          "meal": "Food for Purchase",
          "secure": true
         }
        ]
       }
      ]
     }
    ],
    "pricing": [
     {
      "kind": "qpxexpress#pricingInfo",
      "fare": [
       {
        "kind": "qpxexpress#fareInfo",
        "id": "ATg47OPUOl/jlrBCQY+Z5sVfPAQ3eOAlsRpXTmpA7muk",
        "carrier": "UA",
        "origin": "DEN",
        "destination": "EWR",
        "basisCode": "KEA2AFEN"
       },
       {
        "kind": "qpxexpress#fareInfo",
        "id": "ALslzC00ecQT/lChCiuFK8IMUww94mRl3GtuzFBUOSuA",
        "carrier": "UA",
        "origin": "EWR",
        "destination": "DEN",
        "basisCode": "WFA7AFEN"
       }
      ],
      "segmentPricing": [
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "ALslzC00ecQT/lChCiuFK8IMUww94mRl3GtuzFBUOSuA",
        "segmentId": "Ggukoy1Wdj8JYSnL"
       },
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "ATg47OPUOl/jlrBCQY+Z5sVfPAQ3eOAlsRpXTmpA7muk",
        "segmentId": "Ga+MVN5CvJaw6vwj"
       }
      ],
      "baseFareTotal": "USD398.13",
      "saleFareTotal": "USD398.13",
      "saleTaxTotal": "USD58.27",
      "saleTotal": "USD456.40",
      "passengers": {
       "kind": "qpxexpress#passengerCounts",
       "adultCount": 1
      },
      "tax": [
       {
        "kind": "qpxexpress#taxInfo",
        "id": "US_001",
        "chargeType": "GOVERNMENT",
        "code": "US",
        "country": "US",
        "salePrice": "USD29.87"
       },
       {
        "kind": "qpxexpress#taxInfo",
        "id": "AY_001",
        "chargeType": "GOVERNMENT",
        "code": "AY",
        "country": "US",
        "salePrice": "USD11.20"
       },
       {
        "kind": "qpxexpress#taxInfo",
        "id": "XF",
        "chargeType": "GOVERNMENT",
        "code": "XF",
        "country": "US",
        "salePrice": "USD9.00"
       },
       {
        "kind": "qpxexpress#taxInfo",
        "id": "ZP",
        "chargeType": "GOVERNMENT",
        "code": "ZP",
        "country": "US",
        "salePrice": "USD8.20"
       }
      ],
      "fareCalculation": "DEN UA EWR Q18.60 124.65KEA2AFEN UA DEN Q18.60 236.28WFA7AFEN USD 398.13 END ZP DEN EWR XT 29.87US 8.20ZP 11.20AY 9.00XF DEN4.50 EWR4.50",
      "latestTicketingTime": "2017-02-06T23:59-05:00",
      "ptc": "ADT"
     }
    ]
   },
   {
    "kind": "qpxexpress#tripOption",
    "saleTotal": "USD456.40",
    "id": "3K4245DYagKMD7ZY8rl7iP002",
    "slice": [
     {
      "kind": "qpxexpress#sliceInfo",
      "duration": 209,
      "segment": [
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 209,
        "flight": {
         "carrier": "UA",
         "number": "314"
        },
        "id": "GIKK7WO8C3xG2vrB",
        "cabin": "COACH",
        "bookingCode": "K",
        "bookingCodeCount": 9,
        "marriedSegmentGroup": "0",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "L97EZaqCvK4VTs1c",
          "aircraft": "777",
          "arrivalTime": "2017-04-01T23:29-04:00",
          "departureTime": "2017-04-01T18:00-06:00",
          "origin": "DEN",
          "destination": "EWR",
          "destinationTerminal": "C",
          "duration": 209,
          "onTimePerformance": 90,
          "mileage": 1600,
          "meal": "Food for Purchase",
          "secure": true
         }
        ]
       }
      ]
     },
     {
      "kind": "qpxexpress#sliceInfo",
      "duration": 264,
      "segment": [
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 264,
        "flight": {
         "carrier": "UA",
         "number": "1961"
        },
        "id": "Ggukoy1Wdj8JYSnL",
        "cabin": "COACH",
        "bookingCode": "W",
        "bookingCodeCount": 9,
        "marriedSegmentGroup": "1",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "LdF-m5MFCtnO7Usc",
          "aircraft": "739",
          "arrivalTime": "2017-04-08T20:29-06:00",
          "departureTime": "2017-04-08T18:05-04:00",
          "origin": "EWR",
          "destination": "DEN",
          "originTerminal": "C",
          "duration": 264,
          "onTimePerformance": 80,
          "mileage": 1600,
          "meal": "Food for Purchase",
          "secure": true
         }
        ]
       }
      ]
     }
    ],
    "pricing": [
     {
      "kind": "qpxexpress#pricingInfo",
      "fare": [
       {
        "kind": "qpxexpress#fareInfo",
        "id": "ATg47OPUOl/jlrBCQY+Z5sVfPAQ3eOAlsRpXTmpA7muk",
        "carrier": "UA",
        "origin": "DEN",
        "destination": "EWR",
        "basisCode": "KEA2AFEN"
       },
       {
        "kind": "qpxexpress#fareInfo",
        "id": "ALslzC00ecQT/lChCiuFK8IMUww94mRl3GtuzFBUOSuA",
        "carrier": "UA",
        "origin": "EWR",
        "destination": "DEN",
        "basisCode": "WFA7AFEN"
       }
      ],
      "segmentPricing": [
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "ALslzC00ecQT/lChCiuFK8IMUww94mRl3GtuzFBUOSuA",
        "segmentId": "Ggukoy1Wdj8JYSnL"
       },
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "ATg47OPUOl/jlrBCQY+Z5sVfPAQ3eOAlsRpXTmpA7muk",
        "segmentId": "GIKK7WO8C3xG2vrB"
       }
      ],
      "baseFareTotal": "USD398.13",
      "saleFareTotal": "USD398.13",
      "saleTaxTotal": "USD58.27",
      "saleTotal": "USD456.40",
      "passengers": {
       "kind": "qpxexpress#passengerCounts",
       "adultCount": 1
      },
      "tax": [
       {
        "kind": "qpxexpress#taxInfo",
        "id": "US_001",
        "chargeType": "GOVERNMENT",
        "code": "US",
        "country": "US",
        "salePrice": "USD29.87"
       },
       {
        "kind": "qpxexpress#taxInfo",
        "id": "AY_001",
        "chargeType": "GOVERNMENT",
        "code": "AY",
        "country": "US",
        "salePrice": "USD11.20"
       },
       {
        "kind": "qpxexpress#taxInfo",
        "id": "XF",
        "chargeType": "GOVERNMENT",
        "code": "XF",
        "country": "US",
        "salePrice": "USD9.00"
       },
       {
        "kind": "qpxexpress#taxInfo",
        "id": "ZP",
        "chargeType": "GOVERNMENT",
        "code": "ZP",
        "country": "US",
        "salePrice": "USD8.20"
       }
      ],
      "fareCalculation": "DEN UA EWR Q18.60 124.65KEA2AFEN UA DEN Q18.60 236.28WFA7AFEN USD 398.13 END ZP DEN EWR XT 29.87US 8.20ZP 11.20AY 9.00XF DEN4.50 EWR4.50",
      "latestTicketingTime": "2017-02-06T23:59-05:00",
      "ptc": "ADT"
     }
    ]
   }
  ]
 }
}
"""