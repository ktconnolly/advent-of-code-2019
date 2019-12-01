def read_ints(file):
    with open(file, "r") as f:
        return [int(line.strip()) for line in f.readlines()]
