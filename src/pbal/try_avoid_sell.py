import heapq
from math import copysign
from .strategy import Strategy


class TryAvoidSell(Strategy):
    def _make_strategy(self, positions, cash_to_invest):
        sign = copysign(1, cash_to_invest)
        position_heap = [(sign * v["PositionValue"], k) for k, v in positions.items()]
        heapq.heapify(position_heap)
        increment = 10**self._tol_zeros
        while sign * cash_to_invest >= increment:
            head = heapq.heappop(position_heap)
            edit = head[0] + increment
            new = (edit, head[1])
            heapq.heappush(position_heap, new)
            cash_to_invest -= sign * increment
        for final_val, sym in position_heap:
            init_val = positions[sym]["PositionValue"]
            positions[sym]["BuyVal"] = sign * final_val - init_val
        return positions
