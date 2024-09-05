"""
Sample Tests.
"""
from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    """Tests the calc module."""
    
    def test_add_number(self):
        """Test adding numbers together."""
        res = calc.add(5, 6)
        
        self.assertEqual(res, 11)
        
    def test_subtract_numbers(self):
        """Test subtracting numbers."""
        res calc.subtract(10, 15)
        
        