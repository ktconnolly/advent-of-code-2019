from intcode import Computer


def read(file):
    with open(file, "r") as f:
        return [int(i) for i in f.readline().split(",")]


def part_one():
    c = Computer(read("input.txt"))
    c.add_input(1)

    outputs = []
    while (output := c.run()) is not None:
        outputs.append(output)

    return outputs[-1]


def part_two():
    c = Computer(read("input.txt"))
    c.add_input(5)

    outputs = []
    while (output := c.run()) is not None:
        outputs.append(output)

    return outputs[-1]
