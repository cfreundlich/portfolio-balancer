def load(fname):
    positions = dict()
    with open(fname, "r") as f:
        for l in f.readlines():
            data = l.replace('"', "").rstrip("\n").split(",")
            sym = data[0]
            val = float(data[1])
            positions[sym] = {"initial_value": val}

    return positions
