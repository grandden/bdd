"""
Sample tests for the calc module.
"""
from django.test import SimpleTestCase
from .calc import add


class CalcTests(SimpleTestCase):
    """Tests for the calc module."""

    def test_add_numbers(self):
        """Test adding numbers together."""
        self.assertEqual(add(3, 8), 11)
        self.assertEqual(add(-2, 2), 0)
