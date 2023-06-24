import unittest
from src.pbal.try_avoid_sell import TryAvoidSell
from src.pbal.csv import load


class HardRebalTestCase(unittest.TestCase):
    @staticmethod
    def _basic(cash):
        positions = load("tests/data/basic.csv")
        return TryAvoidSell(positions, cash)

    def test_basic_0_new_investment(self):
        s = self._basic(0.0)
        self.assertEqual(s.proposal["FOO"]["change"], 0.0)
        self.assertEqual(s.proposal["BAR"]["change"], 0.0)

    def test_basic_equalizing_new_investment(self):
        s = self._basic(50000.0)
        self.assertEqual(s.proposal["FOO"]["change"], 50000.0)
        self.assertEqual(s.proposal["BAR"]["change"], 0.0)

    def test_basic_new_money_investment(self):
        s = self._basic(100000.0)
        self.assertEqual(s.proposal["FOO"]["change"], 75000.0)
        self.assertEqual(s.proposal["BAR"]["change"], 25000.0)

    def test_basic_pull_money_out(self):
        s = self._basic(-10000.0)
        self.assertEqual(s.proposal["FOO"]["change"], 0.0)
        self.assertEqual(s.proposal["BAR"]["change"], -10000.0)
