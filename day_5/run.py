def read(file):
    with open(file, "r") as f:
        return [int(i) for i in f.readline().split(",")]


def parse_instruction(instruction):
    return [int(i) for i in str(instruction)[::-1]]


def get_modes(instruction):
    modes = [m for m in instruction[2:]]

    while len(modes) < 3:
        modes.append(0)

    return modes


def run_intcode(code):
    i = 0
    while code[i] != 99:
        instruction = parse_instruction(code[i])

        opcode = instruction[0]
        modes = get_modes(instruction)

        p1 = i + 1 if modes[0] == 1 else code[i + 1]
        p2 = i + 2 if modes[1] == 1 else code[i + 2]
        p3 = i + 3 if modes[2] == 1 else code[i + 3]

        if opcode == 1:
            code[p3] = code[p1] + code[p2]
            i += 4
        elif opcode == 2:
            code[p3] = code[p1] * code[p2]
            i += 4
        elif opcode == 3:
            code[p1] = int(input("input: "))
            i += 2
        elif opcode == 4:
            print(code[p1])
            i += 2
        elif opcode == 5:
            if code[p1] != 0:
                i = code[p2]
            else:
                i += 3
        elif opcode == 6:
            if code[p1] == 0:
                i = code[p2]
            else:
                i += 3
        elif opcode == 7:
            if code[p1] < code[p2]:
                code[p3] = 1
            else:
                code[p3] = 0
            i += 4
        elif opcode == 8:
            if code[p1] == code[p2]:
                code[p3] = 1
            else:
                code[p3] = 0
            i += 4


def part_one():
    pass  # input 1 gives output of 12234644


def part_two():
    pass  # input 5 gives 3output of 508186
