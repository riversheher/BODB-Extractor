import unittest
from extractor import extractor
from datetime import datetime

from models.record import OptionType

class TestConstructRecord(unittest.TestCase):
    """
    This is a test class with a set of integration tests from a top down approach.
    
    Unit tests for each individual function are not included in this class.  They should be
    included in separate test classes.

    """
    config_dict = {
            'host': 'localhost',
            'database': 'bodb',
            'user': 'bodb',
            'password': 'bodb'
        }
        
    def test_nominal_ticker(self):
        """Test a normal, correctly formatted line for the ticker field."""
        
        e = extractor(self.config_dict)
        
        line = " 2AA 800102 90304 1  4500 1000 1050 5500"
        record = e.construct_record(line)
        self.assertEqual(record.ticker, "AA")
        
    def test_nominal_date_time(self):
        """Test a normal, correctly formatted line for the date and time field."""
        
        e = extractor(self.config_dict)
        
        line = " 2AA 800102 90304 1  4500 1000 1050 5500"
        record = e.construct_record(line)
        self.assertEqual(record.timestamp, datetime(1980, 1, 2, 9, 3, 4))
        
    def test_nominal_expiration_date(self):
        """Test a normal, correctly formatted line for the expiration date field."""
        
        e = extractor(self.config_dict)
        
        line = " 2AA 800102 90304 1  4500 1000 1050 5500"
        record = e.construct_record(line)
        self.assertEqual(record.expiration_date, datetime(1980, 1, 19, 0, 0, 0))
        
    def test_nominal_option_type(self):
        """Test a normal, correctly formatted line for the put flag field."""
        
        e = extractor(self.config_dict)
        
        line = " 2AA 800102 90304 1  4500 1000 1050 5500"
        record = e.construct_record(line)
        self.assertEqual(record.option_type, OptionType.call)
        
    def test_nominal_strike_price(self):
        """Test a normal, correctly formatted line for the strike price field."""
        
        e = extractor(self.config_dict)
        
        line = " 2AA 800102 90304 1  4500 1000 1050 5500"
        record = e.construct_record(line)
        self.assertEqual(record.strike_price, 45.00)
        
    def test_nomimal_underlying_price(self):
        """Test a normal, correctly formatted line for the underlying price field."""
        
        e = extractor(self.config_dict)
        
        line = " 1NCR800213123936 3  7000 1013   10 8013"
        record = e.construct_record(line)
        self.assertEqual(record.underlying_price, 80.13)
        
    def test_issue(self):
        e = extractor(self.config_dict)
        record = e.construct_record(" 1OXY800130150522 5  3000  300    1 2925")
        print(f'TESTING RECORD: {str(record)}')
        
if __name__ == "__main__":
    unittest.main()