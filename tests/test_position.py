import unittest
from src.pbal.position import load


class PositionTestCase(unittest.TestCase):

    def test_basic(self):
        positions = load('tests/data/basic.csv')
        self.assertEqual(positions[0].symbol, 'FOO')
        self.assertEqual(positions[0].cash, 50000.)
        self.assertEqual(positions[1].symbol, 'BAR')
        self.assertEqual(positions[1].cash, 100000.)
