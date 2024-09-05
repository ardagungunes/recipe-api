"""
Sample Tests.
"""
from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    """Tests the calc module."""
    
    def test_add_number(self):
        """Test adding numbers together"""