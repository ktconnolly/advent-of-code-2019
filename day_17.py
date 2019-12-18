from intcode import Computer


NORTH = 1
SOUTH = 2
WEST = 3
EAST = 4


def read(file):
    with open(file, "r") as f:
        return [int(i) for i in f.readline().split(",")]


def make_move(position, direction):
    moves = {NORTH: (0, 1), SOUTH: (0, -1), WEST: (-1, 0), EAST: (1, 0)}
    return tuple(map(sum, zip(position, moves.get(direction))))


def get_neighbours(pos):
    return [make_move(pos, direction) for direction in range(1, 5)]


def get_map(comp):
    outputs = []
    row = []
    while not comp.finished:
        out = comp.run()
        if row and out == 10:
            outputs.append(row)
            row = []
        elif out is not None:
            row.append(chr(out))

    return outputs


def part_one():
    computer = Computer(read("inputs/day_17.txt"))
    scaffolding = get_map(computer)

    param_sum = 0

    for row in range(len(scaffolding)):
        for col in range(len(scaffolding[0])):
            if scaffolding[row][col] != "#":
                continue

            try:
                neighbours = [
                    scaffolding[row][col] for (row, col) in
                    get_neighbours((row, col))
                ]
            except IndexError:
                continue

            if len(neighbours) == 4 and all(i == '#' for i in neighbours):
                param_sum += row * col

    return param_sum
