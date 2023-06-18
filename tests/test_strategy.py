import unittest
from src.strategy import Strategy
from src.position import load


class StrategyTestCase(unittest.TestCase):
    
    @staticmethod
    def _basic(cash):
        positions = load('tests/data/basic.csv')
        return Strategy(positions, cash)

    def test_initial_total_value(self):
        self.assertEqual(self._basic(0.).initial_total_value, 150000.)

    def test_basic_0_new_investment(self):
        s = self._basic(0.)
        self.assertEqual(sum(s.buying_strategy().values()), 0.)
        self.assertEqual(s.buying_strategy()['FOO'], 25000.)
        self.assertEqual(s.buying_strategy()['BAR'], -25000.)

    def test_basic_equalizing_new_investment(self):
        s = self._basic(50000.)
        self.assertEqual(sum(s.buying_strategy().values()), 50000.)
        self.assertEqual(s.buying_strategy()['FOO'], 50000.)
        self.assertEqual(s.buying_strategy()['BAR'], 0.)

    def test_basic_new_money_investment(self):
        s = self._basic(100000.)
        self.assertEqual(sum(s.buying_strategy().values()), 100000.)
        self.assertEqual(s.buying_strategy()['FOO'], 75000.)
        self.assertEqual(s.buying_strategy()['BAR'], 25000.)

    def test_basic_pull_money_out(self):
        s = self._basic(-10000.)
        self.assertEqual(sum(s.buying_strategy().values()), -10000.)
        self.assertEqual(s.buying_strategy()['FOO'], 20000.)
        self.assertEqual(s.buying_strategy()['BAR'], -30000.)
