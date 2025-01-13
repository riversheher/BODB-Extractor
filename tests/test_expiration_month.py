import unittest
from datetime import datetime
from internal.expiration_month import get_expiration_date

class TestExpirationDate(unittest.TestCase):
    
    def test_nominal(self):
        test_string = " 2AA 800102 90304 1  4500 1000 1050 5500"
        option_date = datetime(1980, 1, 2)
        month_string = test_string[17:19]
        expiration_date = get_expiration_date(month_string, option_date)
        
        self.assertEqual(expiration_date, datetime(1980, 1, 19))
        
    def test_february(self):
        test_string = " 2AA 810102 90304 2  4500 1000 1050 5500"
        option_date = datetime(1981, 1, 2)
        month_string = test_string[17:19]
        expiration_date = get_expiration_date(month_string, option_date)
        
        self.assertEqual(expiration_date, datetime(1981, 2, 21))
        