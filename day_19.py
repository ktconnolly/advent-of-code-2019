from intcode import Computer


def read(file):
    with open(file, "r") as f:
        return [int(i) for i in f.readline().split(",")]


def beam(x, y):
    c = Computer(read("inputs/day_19.txt"))
    c.add_input(x)
    c.add_input(y)
    return int(c.run())


def part_one():
    return sum(beam(x, y) for x in range(50) for y in range(50))


def part_two():
    x = 0
    y = 0
    while not beam(x, y + 99):
        x += 1
        while not beam(x + 99, y):
            y += 1
    return x + y * 10000
