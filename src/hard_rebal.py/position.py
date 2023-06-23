class Position:
    def __init__(self, symbol, cash):
        self.symbol = symbol
        self.cash = cash

    def buy(self, cash):
        self.cash += cash


def load(fname):
    positions = []
    with open(fname, 'r') as f:
        for l in f.readlines():
            data = l.replace('"', '').rstrip('\n').split(',')
            sym = data[0]
            val = float(data[1])
            positions.append(Position(sym, val))

    return positions
