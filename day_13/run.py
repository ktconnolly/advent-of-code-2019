from intcode import Computer


def read(file):
    with open(file, "r") as f:
        return [int(i) for i in f.readline().split(",")]


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

    for out in computer.run():
        outputs.append(out)

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
    for out in computer.run():
        outputs.append(out)

        if len(outputs) == 3:
            tile = outputs.pop()
            row = outputs.pop()
            col = outputs.pop()

            game.update(row, col, tile)
            computer.add_input(game.get_ai_move())

    return game.score
