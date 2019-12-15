from intcode import Computer


def read(file):
    with open(file, "r") as f:
        return [int(i) for i in f.readline().split(",")]


def part_one():
    c = Computer(read("input.txt"))
    c.add_input(1)
    return next(c.run())


def part_two():
    c = Computer(read("input.txt"))
    c.add_input(2)
    return next(c.run())
