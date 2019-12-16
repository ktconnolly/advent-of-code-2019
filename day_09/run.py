from intcode import Computer


def read(file):
    with open(file, "r") as f:
        return [int(i) for i in f.readline().split(",")]


def part_one():
    c = Computer(read("day_09/input.txt"))
    c.add_input(1)
    return c.run()


def part_two():
    c = Computer(read("day_09/input.txt"))
    c.add_input(2)
    return c.run()
