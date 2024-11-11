import unittest

from date_time import string_to_datetime

class test_string_to_datetime(unittest.TestCase):
    
    def test_standard(self):
        case_1 = "800102 90304"
        
        calculated = string_to_datetime(case_1)
        print(calculated)
        
        self.assertEqual(calculated.year, 1980)
        self.assertEqual(calculated.month, 1)
        self.assertEqual(calculated.day, 2)
        self.assertEqual(calculated.hour, 9)
        self.assertEqual(calculated.minute, 3)
        self.assertEqual(calculated.second, 4)
        
if __name__ == '__main__':
    unittest.main()
        