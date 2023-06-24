import numpy as np
from src.pbal.strategy import Strategy


class HardRebal(Strategy):
    def _target(self, positions):
        return self._target_net_liquidity / len(positions)

    def _make_strategy(self, positions, cash_to_invest):
        A = np.vstack(tup=(np.ones((1, len(positions))), np.eye(len(positions))))

        b = [cash_to_invest]
        keymap = []
        for k, p in positions.items():
            keymap.append(k)
            b.append(self._target(positions) - p["initial_value"])

        # Solve for x in Ax = b using least squares method
        proposed_purchase, _, _, _ = np.linalg.lstsq(A, b, rcond=None)
        # also could do: np.linalg.solve(A, b)

        for k, x in zip(keymap, proposed_purchase):
            positions[k]["change"] = round(x, -self._tol_zeros)

        return positions
