import unittest
from src.pbal.csv import load


class PositionTestCase(unittest.TestCase):
    def test_basic(self):
        positions = load("tests/data/basic.csv")
        self.assertEqual(positions["FOO"]["PositionValue"], 50000.0)
        self.assertEqual(positions["BAR"]["PositionValue"], 100000.0)
