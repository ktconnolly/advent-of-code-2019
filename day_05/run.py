from intcode import Computer


def read(file):
    with open(file, "r") as f:
        return [int(i) for i in f.readline().split(",")]


def part_one():
    c = Computer(read("day_05/input.txt"), inputs=[1])

    outputs = []
    while not c.finished:
        output = c.run()

        if output is not None:
            outputs.append(output)

    return outputs[-1]


def part_two():
    c = Computer(read("day_05/input.txt"), inputs=[5])

    outputs = []
    while not c.finished:
        output = c.run()

        if output is not None:
            outputs.append(output)

    return outputs[-1]
