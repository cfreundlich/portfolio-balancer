import argparse
from pathlib import Path
from tabulate import tabulate
from .hard_rebal import HardRebal
from .try_avoid_sell import TryAvoidSell
from .csv import load



def pbal():
    parser = argparse.ArgumentParser(
        description="A script to initialize a Strategy object and perform operations."
    )

    # positional argument for the data file path with a default value
    DEFAULT_CSV = f"{Path.home()}/Downloads/positions-custom.csv"
    parser.add_argument(
        "data",
        nargs="?",
        default=DEFAULT_CSV,
        help=f'The data file to read. Default is {DEFAULT_CSV}.',
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
    STRATEGIES = {
        'hard_rebalance': HardRebal,
        'try_avoid_sell': TryAvoidSell
    }
    parser.add_argument(
        "-s",
        "--strategy",
        choices=list(STRATEGIES.keys()),
        default="try_avoid_sell",
        help="Strategy to use to rebalance portfolio. Default is try_avoid_sell",
    )

    args = parser.parse_args()

    # use the arguments
    # assuming load function takes data file path as input
    initial_positions = load(args.data)

    # now Strategy is initialized with initial_positions and cash
    strategy = STRATEGIES[args.strategy]

    # pprint(strategy(initial_positions, args.cash).proposal)
    proposal = strategy(initial_positions, args.cash).proposal
    table = [['symbol', 'initial_value', 'change']]
    table += [[k, v['initial_value'], v['change']] for k,v in proposal.items()]
    print(tabulate(table))
