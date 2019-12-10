from itertools import permutations


def read(file):
    with open(file, "r") as f:
        return [int(i) for i in f.readline().split(",")]


class Program:
    def __init__(self, code, setting):
        self.code = code.copy()
        self.inputs = [setting]
        self.i = 0

    def get_opcode(self):
        return self.code[self.i] % 100

    def get_param(self, n):
        if self.i + n > len(self.code) - 1:
            return None

        if self.get_mode(n) == 1:
            return self.i + n
        else:
            return self.code[self.i + n]

    def get_mode(self, n):
        return self.code[self.i] // (10 ** (1 + n)) % 10

    def run(self, inputs):
        self.inputs += inputs

        while self.i < len(self.code):
            op = self.get_opcode()

            if op == 99:
                break

            p1, p2, p3 = [self.get_param(p) for p in range(1, 4)]

            if op == 1:
                self.code[p3] = self.code[p1] + self.code[p2]
                self.i += 4
            elif op == 2:
                self.code[p3] = self.code[p1] * self.code[p2]
                self.i += 4
            elif op == 3:
                self.code[p1] = self.inputs.pop(0)
                self.i += 2
            elif op == 4:
                self.i += 2
                return self.code[p1]
            elif op == 5:
                self.i = self.code[p2] if self.code[p1] != 0 else self.i + 3
            elif op == 6:
                self.i = self.code[p2] if self.code[p1] == 0 else self.i + 3
            elif op == 7:
                self.code[p3] = int(self.code[p1] < self.code[p2])
                self.i += 4
            elif op == 8:
                self.code[p3] = int(self.code[p1] == self.code[p2])
                self.i += 4
            else:
                raise Exception("Invalid opcode")


def part_one():
    code = read("input.txt")
    outputs = []

    for settings in permutations(range(5)):
        amps = [Program(code, setting) for setting in settings]

        output = 0
        for amp in amps:
            output = amp.run(inputs=[output])

        outputs.append(output)

    return max(outputs)


def part_two():
    code = read("input.txt")
    outputs = []

    for settings in permutations(range(5, 10)):
        amps = [Program(code, setting) for setting in settings]

        output = 0
        while output is not None:
            outputs.append(output)
            for amp in amps:
                output = amp.run([output])

    return max(outputs)
