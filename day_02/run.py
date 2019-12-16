def read(file):
    with open(file, "r") as f:
        return [int(i) for i in f.readline().split(",")]


def run_intcode(code, noun, verb):
    code[1] = noun
    code[2] = verb

    i = 0
    while code[i] != 99:
        p1, p2, p3 = code[i + 1: i + 4]

        if code[i] == 1:
            code[p3] = code[p1] + code[p2]
        elif code[i] == 2:
            code[p3] = code[p1] * code[p2]

        i += 4

    return code[0]


def part_one():
    code = read("day_02/input.txt")
    return run_intcode(code, noun=12, verb=2)


def part_two():
    original = read("day_02/input.txt")

    for noun in range(100):
        for verb in range(100):
            code = list(original)

            if run_intcode(code, noun, verb) == 19690720:
                return 100 * noun + verb
