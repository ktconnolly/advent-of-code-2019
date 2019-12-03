def read(file):
    with open(file, "r") as f:
        return [[i.strip() for i in line.split(",")] for line in f]


def make_move(position, direction):
    moves = {"U": (1, 0), "D": (-1, 0), "R": (0, 1), "L": (0, -1)}
    return tuple(map(sum, zip(position, moves.get(direction))))


def get_points(wire):
    position = (0, 0)
    steps = 0
    points = {}
    for i in wire:
        for _ in range(int(i[1:])):
            steps += 1
            position = make_move(position, direction=i[0])

            if position not in points:
                points[position] = steps

    return points


w1, w2 = read("input.txt")

steps1 = get_points(w1)
steps2 = get_points(w2)

intersects = steps1.keys() & steps2.keys()


def part_one():
    return min(abs(p1) + abs(p2) for p1, p2 in intersects)


def part_two():
    return min(steps1[p] + steps2[p] for p in intersects)
