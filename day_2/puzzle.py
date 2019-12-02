def read_ints(file):
    with open(file, "r") as f:
        return [int(i) for i in f.readline().split(",")]


def run_intcode(code):
    i = 0

    while i < len(code):
        p1 = code[i + 1]
        p2 = code[i + 2]
        p3 = code[i + 3]

        if code[i] == 1:
            code[p3] = code[p1] + code[p2]
        elif code[i] == 2:
            code[p3] = code[p1] * code[p2]
        elif code[i] == 99:
            break

        i += 4

    return code[0]


def part_one():
    program = read_ints("input.txt")
    program[1] = 12
    program[2] = 2
    return run_intcode(program)


def part_two():
    original = read_ints("input.txt")

    for noun in range(100):
        for verb in range(100):
            program = list(original)
            program[1] = noun
            program[2] = verb

            if run_intcode(program) == 19690720:
                return 100 * noun + verb
