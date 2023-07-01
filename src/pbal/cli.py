import argparse
from pathlib import Path
from tabulate import tabulate
from .hard_rebal import HardRebal
from .try_avoid_sell import TryAvoidSell
from .csv import load


STRATEGIES = {"hard_rebalance": HardRebal, "try_avoid_sell": TryAvoidSell}
DEFAULT_CSV = f"{Path.home()}/Downloads/positions-custom.csv"


def _parser():
    parser = argparse.ArgumentParser(
        description="A script to help make trading decisions on a brokerage account."
    )

    # positional argument for the data file path with a default value

    parser.add_argument(
        "data",
        nargs="?",
        default=DEFAULT_CSV,
        help=f"The file containing portfolio data. Default is {DEFAULT_CSV}.",
    )

    # named argument for the cash to invest
    parser.add_argument(
        "-c",
        "--cash",
        type=float,
        default=0.0,
        help="The amount of cash to invest. Default is 0.  Negative values mean you want to free up some cash.  Positive values mean you have some more cash or margin you want to invest",
    )

    # named argument for the minimum increment of cash to invest at a time
    parser.add_argument(
        "-i",
        "--increment",
        choices=range(1, 5),
        default=3,
        type=int,
        help="The minimal investment amount order of magnitude. This avoids suggesting small transactions. Default is 3, which corresponds to $1000. Setting this arg to anything than 1 might lead to overinvesting by less than the order of magnitude of the increment",
    )

    # named argument for the strategy to employ
    parser.add_argument(
        "-s",
        "--strategy",
        choices=list(STRATEGIES.keys()),
        default="try_avoid_sell",
        help="Strategy to use to rebalance portfolio. Default is try_avoid_sell.  See https://github.com/cfreundlich/portfolio-balancer and look at code for details.",
    )

    # named argument for verbosity
    parser.add_argument(
        "-v",
        "--verbose",
        action='store_true',
        help="Control printing",
    )

    return parser.parse_args()


def pbal():
    args = _parser()

    # use the arguments
    # assuming load function takes data file path as input
    initial_positions = load(args.data)

    # now Strategy is initialized with initial_positions and cash
    strategy = STRATEGIES[args.strategy]

    # pprint(strategy(initial_positions, args.cash).proposal)
    s = strategy(initial_positions, args.cash, args.verbose, args.increment)

    table = s.table()
    print(tabulate(table[1:], headers=table[0]))
