import logging


logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger()


class Strategy:
    def __init__(self, positions, cash_to_invest=0.0, tol_zeros=3):
        self._tol_zeros = 3
        self._target_net_liquidity = cash_to_invest + sum(
            v["PositionValue"] for v in positions.values()
        )
        self.proposal = self._make_strategy(positions, cash_to_invest)

    def _make_strategy(self, positions, cash_to_invest):
        raise NotImplementedError

    def table(self):
        table = [["Symbol", "PositionValue", "MarkPrice", "BuyVal", "BuyShares"]]
        for val in self.proposal.values():
            row = [p for k, p in val.items() if k in table[0]]
            row.append(round(val["BuyVal"] / val["MarkPrice"]))
            table.append(row)

        i = table[0].index("PositionValue")
        table[0][i] = "InitialValue"
        return table
