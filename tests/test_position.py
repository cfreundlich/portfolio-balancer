import unittest
from src.pbal.csv import load


class PositionTestCase(unittest.TestCase):
    def test_basic(self):
        positions = load("tests/data/basic.csv")
        self.assertEqual(positions["FOO"]["initial_value"], 50000.0)
        self.assertEqual(positions["BAR"]["initial_value"], 100000.0)
