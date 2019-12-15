from intcode import Computer


def read(file):
    with open(file, "r") as f:
        return [int(i) for i in f.readline().split(",")]


def part_one():
    c = Computer(read("input.txt"))
    c.add_input(1)

    for out in c.run():
        pass

    return out


def part_two():
    c = Computer(read("input.txt"))
    c.add_input(5)

    for out in c.run():
        pass

    return out
