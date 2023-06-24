import logging

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger()


class Strategy:
    def __init__(self, positions, cash_to_invest=0.0, tol_zeros=3):
        self._tol_zeros = 3
        self._target_net_liquidity = cash_to_invest + sum(
            v["initial_value"] for v in positions.values()
        )
        self.proposal = self._make_strategy(positions, cash_to_invest)

    def _make_strategy(self, positions, cash_to_invest):
        raise NotImplementedError
