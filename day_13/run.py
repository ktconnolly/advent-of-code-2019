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
                self.set_param(1, self.inputs.pop())
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


class Game:
    def __init__(self):
        self.display = {}
        self.score = 0
        self.ball_col = 0
        self.paddle_col = 0

    def set_score(self, points):
        self.score = points

    def update(self, row, col, tile):
        if col == -1:
            self.score = tile
        else:
            self.display[(row, col)] = tile

            if tile == 4:
                self.ball_col = col
            elif tile == 3:
                self.paddle_col = col

    def get_ai_move(self):
        if self.ball_col < self.paddle_col:
            return -1
        elif self.ball_col > self.paddle_col:
            return 1
        else:
            return 0


def part_one():
    computer = Computer(read("input.txt"))
    game = Game()
    outputs = []
    for i in computer.run():
        outputs.append(i)

        if len(outputs) == 3:
            tile = outputs.pop()
            row = outputs.pop()
            col = outputs.pop()
            game.update(row, col, tile)

    return sum(c == 2 for c in game.display.values())


def part_two():
    computer = Computer(read("input.txt"))
    computer.write(index=0, val=2)

    game = Game()
    outputs = []
    for i in computer.run():
        outputs.append(i)

        if len(outputs) == 3:
            tile = outputs.pop()
            row = outputs.pop()
            col = outputs.pop()

            game.update(row, col, tile)
            computer.add_input(game.get_ai_move())

    return game.score
