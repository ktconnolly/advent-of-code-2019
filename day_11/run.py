from collections import defaultdict

from intcode import Computer


def read(file):
    with open(file, "r") as f:
        return [int(i) for i in f.readline().split(",")]


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
    while (output := painter.run()) is not None:
        outputs.append(output)

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
