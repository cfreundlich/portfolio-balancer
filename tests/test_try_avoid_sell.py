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
        self.assertEqual(s.proposal["FOO"]["BuyVal"], 0.0)
        self.assertEqual(s.proposal["BAR"]["BuyVal"], 0.0)

    def test_basic_equalizing_new_investment(self):
        s = self._basic(50000.0)
        self.assertEqual(s.proposal["FOO"]["BuyVal"], 50000.0)
        self.assertEqual(s.proposal["BAR"]["BuyVal"], 0.0)

    def test_basic_new_money_investment(self):
        s = self._basic(100000.0)
        self.assertEqual(s.proposal["FOO"]["BuyVal"], 75000.0)
        self.assertEqual(s.proposal["BAR"]["BuyVal"], 25000.0)

    def test_basic_pull_money_out(self):
        s = self._basic(-10000.0)
        self.assertEqual(s.proposal["FOO"]["BuyVal"], 0.0)
        self.assertEqual(s.proposal["BAR"]["BuyVal"], -10000.0)

    def test_cap_loss_tiebreaker(self):
        positions = load("tests/data/caploss-foo.csv")
        s = TryAvoidSell(positions, -1000)
        self.assertEqual(s.proposal["FOO"]["BuyVal"], -1000.0)
        self.assertEqual(s.proposal["BAR"]["BuyVal"], 0)
        self.assertEqual(s.proposal["BUZ"]["BuyVal"], 0)

    def test_cap_loss_tiebreaker(self):
        positions = load("tests/data/caploss-bar.csv")
        s = TryAvoidSell(positions, -1000)
        self.assertEqual(s.proposal["FOO"]["BuyVal"], 0)
        self.assertEqual(s.proposal["BAR"]["BuyVal"], -1000.0)
        self.assertEqual(s.proposal["BUZ"]["BuyVal"], 0)

    def test_cap_loss_tiebreaker(self):
        positions = load("tests/data/caploss-buz.csv")
        s = TryAvoidSell(positions, -1000)
        self.assertEqual(s.proposal["FOO"]["BuyVal"], 0)
        self.assertEqual(s.proposal["BAR"]["BuyVal"], 0)
        self.assertEqual(s.proposal["BUZ"]["BuyVal"], -1000.0)

