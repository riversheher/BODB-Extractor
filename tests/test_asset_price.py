import unittest
from internal.asset_price import price_to_dollars_cents

class TestPriceToDollarsCents(unittest.TestCase):

    def test_normal_value(self):
        """Test a normal, correctly formatted asset price string."""
        result = price_to_dollars_cents("05140")
        expected = 51.4
        self.assertEqual(result, expected)
        
    def test_value_with_whitespaces(self):
        """Tests values with filler spaces as described by the BODB guide"""
        result = price_to_dollars_cents(" 5140")
        expected = 51.4
        self.assertEqual(result, expected)
        
if __name__ == "__main__":
    unittest.main()
