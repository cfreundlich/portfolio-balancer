import heapq
from src.pbal.strategy import Strategy


class NeverSell(Strategy):
    def _make_strategy(self, positions, cash_to_invest):
        position_heap = [(v["initial_value"], k) for k, v in positions.items()]
        increment = 10**self._tol_zeros
        while cash_to_invest >= increment:
            heapq.heapify(position_heap)
            position_heap[0] = (position_heap[0][0] + increment, position_heap[0][1])
            cash_to_invest -= increment
        for final_val, sym in position_heap:
            init_val = positions[sym]["initial_value"]
            positions[sym]["change"] = final_val - init_val
        return positions
