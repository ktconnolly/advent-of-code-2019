def read(file):
    with open(file, "r") as f:
        return [int(i) for i in f.readline().split(",")]


class Computer:
    def __init__(self, code):
        self.code = code.copy()
        self.relative_base = 0
        self.i = 0

    def get_opcode(self):
        return self.code[self.i] % 100

    def get_mode(self, n):
        return self.code[self.i] // (10 ** (1 + n)) % 10

    def get_param(self, param_num):
        mode = self.get_mode(param_num)
        index = self.code[self.i + param_num]

        if mode == 0:
            return self.code[index]
        if mode == 1:
            return index
        if mode == 2:
            return self.code[index + self.relative_base]

    def resize(self, n):
        self.code += [0 for _ in range(n - len(self.code) + 1)]

    def write(self, index, val):
        if index > len(self.code) - 1:
            self.resize(index)

        self.code[index] = val

    def set_param(self, param_num, val):
        mode = self.get_mode(param_num)
        index = self.code[self.i + param_num]

        if mode == 0:
            self.write(index, val)
        elif mode == 2:
            self.write(index + self.relative_base, val)

    def run(self, inputs):
        while self.i < len(self.code):
            op = self.get_opcode()

            if op == 99:
                break

            if op == 1:
                self.set_param(3, self.get_param(1) + self.get_param(2))
                self.i += 4
            elif op == 2:
                self.set_param(3, self.get_param(1) * self.get_param(2))
                self.i += 4
            elif op == 3:
                self.set_param(1, inputs.pop(0))
                self.i += 2
            elif op == 4:
                yield self.get_param(1)
                self.i += 2
            elif op == 5:
                self.i = self.get_param(2) if self.get_param(1) != 0 else self.i + 3
            elif op == 6:
                self.i = self.get_param(2) if self.get_param(1) == 0 else self.i + 3
            elif op == 7:
                self.set_param(3, int(self.get_param(1) < self.get_param(2)))
                self.i += 4
            elif op == 8:
                self.set_param(3, int(self.get_param(1) == self.get_param(2)))
                self.i += 4
            elif op == 9:
                self.relative_base += self.get_param(1)
                self.i += 2
            else:
                raise Exception("Invalid opcode")


def part_one():
    c = Computer(read("input.txt"))
    return next(c.run([1]))


def part_two():
    c = Computer(read("input.txt"))
    return next(c.run([2]))
