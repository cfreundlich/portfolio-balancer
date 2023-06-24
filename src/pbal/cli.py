import argparse
from pprint import pprint
from src.pbal.hard_rebal import HardRebal
from src.pbal.try_avoid_sell import TryAvoidSell
from src.pbal.csv import load


def pbal():
    parser = argparse.ArgumentParser(
        description="A script to initialize a Strategy object and perform operations."
    )

    # positional argument for the data file path with a default value
    parser.add_argument(
        "data",
        nargs="?",
        default="data/positions-custom.csv",
        help='The data file to read. Default is "data/positions-custom.csv".',
    )

    # named argument for the cash to invest
    parser.add_argument(
        "-c",
        "--cash",
        type=float,
        default=0.0,
        help="The amount of cash to invest. Default is 0.",
    )

    # named argument for the strategy to employ
    parser.add_argument(
        "-s",
        "--strategy",
        choices=["hard_rebalance", "h", "try_avoid_sell", "t"],
        default="never_sell",
        help="Strategy to use to rebalance portfolio. Default is try_avoid_sell",
    )

    args = parser.parse_args()

    # use the arguments
    # assuming load function takes data file path as input
    initial_positions = load(args.data)

    # now Strategy is initialized with initial_positions and cash
    if args.strategy in {"hard_rebalance", "h"}:
        strategy = HardRebal
    elif args.strategy in {"try_avoid_sell", "t"}:
        strategy = TryAvoidSell
    else:
        raise ValueError(args.strategy)

    pprint(strategy(initial_positions, args.cash).proposal)
