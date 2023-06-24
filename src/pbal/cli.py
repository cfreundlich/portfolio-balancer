import argparse
from pprint import pprint
from src.pbal.hard_rebal import HardRebal
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
        type=str,
        default="hard_rebal",
        help="Strategy to use to rebalance portfolio. Default is hard_rebal",
    )

    args = parser.parse_args()

    # use the arguments
    # assuming load function takes data file path as input
    initial_positions = load(args.data)
    # now Strategy is initialized with initial_positions and cash
    strategy = HardRebal(initial_positions, args.cash)

    pprint(strategy.proposal)
