import numpy as np
import logging


logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger()


class Strategy:
    def __init__(self, initial_positions, cash_to_invest=0.):
        self.cash_to_invest = cash_to_invest
        self.n = len(initial_positions)
        self.initial_positions = initial_positions
        self.tol_zeros = 3
        self.proposed_purchase = self._make_strategy()

    @property
    def initial_total_value(self):
        return sum([position.cash for position in self.initial_positions])

    def buying_strategy(self):
        return {p.symbol: round(v, -self.tol_zeros)
                for p, v in zip(self.initial_positions, self.proposed_purchase)}

    def _total_funds(self):
        return self.initial_total_value + self.cash_to_invest

    def _desired_investment_per_symbol(self):
        return self._total_funds() / self.n

    def _make_strategy(self):

        # try to make 
        Q1 = np.hstack(tup=(
            np.eye(self.n - 1),
            np.zeros((self.n-1, 1))
        ))
        Q2 = np.hstack(tup=(
            np.zeros((self.n-1, 1)),
            np.eye(self.n - 1)
        ))
        Q = Q1 - Q2


        p = np.array([p_i.cash for p_i in self.initial_positions])


    def print_strategy(self):
        print('----\nStrategy:')
        for k, v in sorted(self.buying_strategy().items(), key=lambda x: x[-1]):
            print(f'{k}\t{v}')

    def print_initial_values(self):
        print('----\nInitial positions')
        for p in sorted(self.initial_positions, key=lambda x: -x.cash):
            print(f'{p.symbol}\t{p.cash}')
