from intcode import Computer


def read(file):
    with open(file, "r") as f:
        return [int(i) for i in f.readline().split(",")]


def beam(x, y):
    c = Computer(read("inputs/day_19.txt"))
    c.add_input(x)
    c.add_input(y)
    return c.run()


def part_one():
    return sum(beam(x, y) == 1 for x in range(50) for y in range(50))
