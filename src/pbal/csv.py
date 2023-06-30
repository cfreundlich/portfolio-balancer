import csv


def load(fname):
    # {'Symbol': 'FOO', 'PositionValue': '100.6', 'MarkPrice': '100.4', 'FifoPnlUnrealized': '30.2873'}
    with open(fname, "r") as csvfile:
        reader = csv.DictReader(csvfile)

        positions = dict()
        for p in reader:
            for k in ["PositionValue", "MarkPrice", "FifoPnlUnrealized"]:
                p[k] = float(p[k])
            positions[p["Symbol"]] = p

        return positions
