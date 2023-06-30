import heapq
from math import copysign
from .strategy import Strategy


class TryAvoidSell(Strategy):
    """which will only buy assets to try to approach the target.  It raises the
    floor of your portfolio, buying low incrementally.  This avoids incurring
    capital gains taxes.  If you tell this strategy to free up case (giving
    the case option a negative sign), then it will sell your highest value
    assets first, using capital gains tax exposure as a tie-breaker."""

    def _make_strategy(self, positions, cash_to_invest):
        sign = copysign(1, cash_to_invest)
        position_heap = [
            (sign * v["PositionValue"], v["FifoPnlUnrealized"], k)
            for k, v in positions.items()
        ]
        heapq.heapify(position_heap)
        increment = 1000
        while sign * cash_to_invest >= increment:
            head = heapq.heappop(position_heap)
            edit = head[0] + increment
            new = (edit, head[1] + increment, head[2])
            heapq.heappush(position_heap, new)
            cash_to_invest -= sign * increment
        for final_val, _, sym in position_heap:
            init_val = positions[sym]["PositionValue"]
            positions[sym]["BuyVal"] = sign * final_val - init_val
        return positions
