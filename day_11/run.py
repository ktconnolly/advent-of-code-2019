from collections import defaultdict


def read(file):
    with open(file, "r") as f:
        return [int(i) for i in f.readline().split(",")]


class Computer:
    def __init__(self, code):
        self.code = code.copy()
        self.ptr = 0
        self.relative_base = 0
        self.inputs = []

    def add_input(self, inp):
        self.inputs.append(inp)

    def get_opcode(self):
        return self.code[self.ptr] % 100

    def get_mode(self, n):
        return self.code[self.ptr] // (10 ** (1 + n)) % 10

    def get_param(self, param_num):
        mode = self.get_mode(param_num)
        index = self.code[self.ptr + param_num]

        if mode == 0:
            return self.read(index)
        elif mode == 1:
            return index
        elif mode == 2:
            return self.read(index + self.relative_base)
        else:
            raise Exception("Invalid mode")

    def set_param(self, param_num, val):
        mode = self.get_mode(param_num)
        index = self.code[self.ptr + param_num]

        if mode == 0:
            self.write(index, val)
        elif mode == 2:
            self.write(index + self.relative_base, val)
        else:
            raise Exception("Invalid mode")

    def read(self, index):
        if index > len(self.code) - 1:
            self.resize(index)

        return self.code[index]

    def write(self, index, val):
        if index > len(self.code) - 1:
            self.resize(index)

        self.code[index] = val

    def resize(self, index):
        self.code += [0 for _ in range(index - len(self.code) + 1)]

    def run(self):
        while self.ptr < len(self.code):
            op = self.get_opcode()
            if op == 99:
                break

            if op == 1:
                self.set_param(3, self.get_param(1) + self.get_param(2))
                self.ptr += 4
            elif op == 2:
                self.set_param(3, self.get_param(1) * self.get_param(2))
                self.ptr += 4
            elif op == 3:
                self.set_param(1, self.inputs.pop(0))
                self.ptr += 2
            elif op == 4:
                yield self.get_param(1)
                self.ptr += 2
            elif op == 5:
                self.ptr = self.get_param(2) if self.get_param(1) != 0 else self.ptr + 3
            elif op == 6:
                self.ptr = self.get_param(2) if self.get_param(1) == 0 else self.ptr + 3
            elif op == 7:
                self.set_param(3, int(self.get_param(1) < self.get_param(2)))
                self.ptr += 4
            elif op == 8:
                self.set_param(3, int(self.get_param(1) == self.get_param(2)))
                self.ptr += 4
            elif op == 9:
                self.relative_base += self.get_param(1)
                self.ptr += 2
            else:
                raise Exception("Invalid opcode")


def make_move(position, direction):
    # 0 up, 2 down, 1 right, 3 left
    moves = {0: (1, 0), 2: (-1, 0), 1: (0, 1), 3: (0, -1)}
    return tuple(map(sum, zip(position, moves.get(direction))))


def make_turn(curr, turn):
    if turn == 0:
        return (curr - 1) % 4
    else:
        return (curr + 1) % 4


def get_painted_panels(starting_panel):
    painter = Computer(read("input.txt"))
    painter.add_input(starting_panel)

    panels = defaultdict(int)
    direction = 0
    position = (0, 0)

    outputs = []
    for out in painter.run():
        outputs.append(out)

        if len(outputs) == 2:
            turn = outputs.pop()
            colour = outputs.pop()

            panels[position] = colour

            direction = make_turn(direction, turn)
            position = make_move(position, direction)

            painter.add_input(panels[position])

    return panels


def part_one():
    panels = get_painted_panels(0)
    return len(panels.keys())


def part_two():
    panels = get_painted_panels(1)

    max_row = abs(max(panels.keys(), key=lambda panel: abs(panel[0]))[0])
    max_col = abs(max(panels.keys(), key=lambda panel: abs(panel[1]))[1])

    canvas = [[" " for _ in range(max_col)] for _ in range(max_row + 1)]
    for p in panels.keys():
        if panels[p] == 1:
            canvas[abs(p[0])][abs(p[1])] = '#'

    return ["".join(row) for row in canvas]
