"""
Sample tests.
"""

from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    """Tests for the calculator module."""

    def test_add_numbers(self):
        """Test adding two numbers."""
        res = calc.add(3, 5)
        self.assertEqual(res, 8)

    def test_add_negative_numbers(self):
        """Test adding two negative numbers."""
        res = calc.add(-2, -3)
        self.assertEqual(res, -5)
