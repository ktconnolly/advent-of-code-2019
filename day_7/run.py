from itertools import permutations


def read(file):
    with open(file, "r") as f:
        return [int(i) for i in f.readline().split(",")]


class Program:
    def __init__(self, code):
        self.code = code.copy()
        self.i = 0

    def run(self, inputs):
        while self.i < len(self.code):
            op = self.code[self.i] % 100
            m1 = (self.code[self.i] // 100) % 10
            m2 = (self.code[self.i] // 1000) % 10
            m3 = (self.code[self.i] // 10000) % 10

            if op == 99:
                break

            p1, p2, p3 = None, None, None

            if op in (1, 2, 7, 8):
                p1 = self.i + 1 if m1 == 1 else self.code[self.i + 1]
                p2 = self.i + 2 if m2 == 1 else self.code[self.i + 2]
                p3 = self.i + 3 if m3 == 1 else self.code[self.i + 3]
            elif op in (3, 4):
                p1 = self.i + 1 if m1 == 1 else self.code[self.i + 1]
            elif op in (5, 6):
                p1 = self.i + 1 if m1 == 1 else self.code[self.i + 1]
                p2 = self.i + 2 if m2 == 1 else self.code[self.i + 2]

            if op == 1:
                self.code[p3] = self.code[p1] + self.code[p2]
                self.i += 4
            elif op == 2:
                self.code[p3] = self.code[p1] * self.code[p2]
                self.i += 4
            elif op == 3:
                self.code[p1] = inputs.pop(0)
                self.i += 2
            elif op == 4:
                self.i += 2
                return self.code[p1]
            elif op == 5:
                if self.code[p1] != 0:
                    self.i = self.code[p2]
                else:
                    self.i += 3
            elif op == 6:
                if self.code[p1] == 0:
                    self.i = self.code[p2]
                else:
                    self.i += 3
            elif op == 7:
                if self.code[p1] < self.code[p2]:
                    self.code[p3] = 1
                else:
                    self.code[p3] = 0
                self.i += 4
            elif op == 8:
                if self.code[p1] == self.code[p2]:
                    self.code[p3] = 1
                else:
                    self.code[p3] = 0
                self.i += 4


def part_one():
    code = read("input.txt")
    outputs = []

    for settings in permutations(range(5)):
        amps = [Program(code) for _ in range(5)]

        output = 0
        for amp, setting in zip(amps, settings):
            output = amp.run(inputs=[setting, output])

        outputs.append(output)

    return max(outputs)


def part_two():
    code = read("input.txt")
    outputs = []

    for settings in permutations(range(5, 10)):
        amps = [Program(code) for _ in range(5)]

        output = 0
        for amp, setting in zip(amps, settings):
            output = amp.run(inputs=[setting, output])

        while True:
            for amp in amps:
                output = amp.run([output])

            if output:
                outputs.append(output)
            else:
                break

    return max(outputs)
