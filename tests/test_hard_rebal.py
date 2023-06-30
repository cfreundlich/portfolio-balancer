import unittest
from src.pbal.hard_rebal import HardRebal
from src.pbal.csv import load


class HardRebalTestCase(unittest.TestCase):
    @staticmethod
    def _basic(cash):
        positions = load("tests/data/basic.csv")
        return HardRebal(positions, cash)

    def test_basic_0_new_investment(self):
        s = self._basic(0.0)
        self.assertEqual(s.proposal["FOO"]["BuyVal"], 25000.0)
        self.assertEqual(s.proposal["BAR"]["BuyVal"], -25000.0)

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
        self.assertEqual(s.proposal["FOO"]["BuyVal"], 20000.0)
        self.assertEqual(s.proposal["BAR"]["BuyVal"], -30000.0)

    def test_table(self):
        s = self._basic(50000.0)
        table = s.table()
        self.assertListEqual(
            ["Symbol", "InitialValue", "MarkPrice", "BuyVal", "BuyShares"], table[0]
        )
        self.assertListEqual(["FOO", 50000.0, 10.0], table[1][:-2])
        self.assertListEqual(["BAR", 100000.0, 5.0], table[2][:-2])

        self.assertListEqual([50000.0, 5000], table[1][-2:])
        self.assertListEqual([0.0, 0], table[2][-2:])
