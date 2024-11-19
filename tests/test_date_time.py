import unittest
from datetime import datetime
from internal.date_time import string_to_datetime

class TestStringToDateTime(unittest.TestCase):

    def test_normal_value(self):
        """Test a normal, correctly formatted date string."""
        result = string_to_datetime("920922142911")
        expected = datetime(1992, 9, 22, 14, 29, 11)
        self.assertEqual(result, expected)

    def test_unexpected_whitespace(self):
        """Test date string with unexpected leading and trailing whitespaces."""
        result = string_to_datetime(" 920922142911 ")
        expected = datetime(1992, 9, 22, 14, 29, 11)
        self.assertEqual(result, expected)

    def test_unexpected_length(self):
        """Test date string with incorrect length (too short)."""
        with self.assertRaises(ValueError):
            string_to_datetime("92092")  # Missing characters

    def test_invalid_characters(self):
        """Test date string with non-numeric characters."""
        with self.assertRaises(ValueError):
            string_to_datetime("92AA22142911")  # Contains letters instead of numbers

    def test_invalid_date(self):
        """Test date string with an invalid date (e.g., 32nd day of the month)."""
        with self.assertRaises(ValueError):
            string_to_datetime("921332142911")  # Invalid day (32nd)

    def test_edge_case_new_year(self):
        """Test date string at the edge of a year (e.g., midnight on Jan 1)."""
        result = string_to_datetime("900101000000")
        expected = datetime(1990, 1, 1, 0, 0, 0)
        self.assertEqual(result, expected)

    def test_edge_case_end_of_day(self):
        """Test date string at the edge of a day (e.g., 23:59:59)."""
        result = string_to_datetime("920922235959")
        expected = datetime(1992, 9, 22, 23, 59, 59)
        self.assertEqual(result, expected)
        
    def test_whitespace_middle(self):
        """Test date string with whitespace in the middle.
        This is an expected case, extracted from BODB res17 file."""
        result = string_to_datetime("800102 90304")
        expected = datetime(1980, 1, 2, 9, 3, 4)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
