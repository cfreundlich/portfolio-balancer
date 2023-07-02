from .strategy import Strategy


class HardRebal(Strategy):
    '''Sell and buy in order to equalize the values all assets in 
    your portfolio, adding or freeing up cash depending on the user input for 
    cash'''
    def _target(self, positions):
        return self._target_net_liquidity / len(positions)

    def _make_strategy(self, positions, cash_to_invest):
        for k, p in positions.items():
            positions[k]["BuyVal"] = round(self._target(positions) - p["PositionValue"], -self.increment)

        return positions
