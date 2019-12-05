def read(file):
    with open(file, "r") as f:
        return [int(i) for i in f.readline().split(",")]


def run_intcode(code, user_input):
    outputs = []

    i = 0
    while code[i] != 99:
        op = code[i] % 100
        m1 = (code[i] // 100) % 10
        m2 = (code[i] // 1000) % 10
        m3 = (code[i] // 10000) % 10

        p1 = i + 1 if m1 == 1 else code[i + 1]
        p2 = i + 2 if m2 == 1 else code[i + 2]
        p3 = i + 3 if m3 == 1 else code[i + 3]

        if op == 1:
            code[p3] = code[p1] + code[p2]
            i += 4
        elif op == 2:
            code[p3] = code[p1] * code[p2]
            i += 4
        elif op == 3:
            code[p1] = user_input
            i += 2
        elif op == 4:
            outputs.append(code[p1])
            i += 2
        elif op == 5:
            if code[p1] != 0:
                i = code[p2]
            else:
                i += 3
        elif op == 6:
            if code[p1] == 0:
                i = code[p2]
            else:
                i += 3
        elif op == 7:
            if code[p1] < code[p2]:
                code[p3] = 1
            else:
                code[p3] = 0
            i += 4
        elif op == 8:
            if code[p1] == code[p2]:
                code[p3] = 1
            else:
                code[p3] = 0
            i += 4

    return outputs[-1]


def part_one():
    return run_intcode(read("input.txt"), 1)


def part_two():
    return run_intcode(read("input.txt"), 5)