from src.strategy import Strategy, Position
import logging


logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger()


s = Strategy(_)
s.make_strategy()
if not s.buy_uses_cash():
    LOGGER.warn('not all cash used')
if s.buys_too_much():
    LOGGER.warn(
        f'stategy proposes to buy {s.proposed_total_investment()},'
        f' which is more than the initial investment {s.cash_to_invest}'
    )
for k, v in sorted(s.buying_strategy().items(), key=lambda x: x[-1]):
    print(f'{k}\t{v}')
