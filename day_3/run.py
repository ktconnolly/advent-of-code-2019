def read(file):
    with open(file, "r") as f:
        return [[i.strip() for i in line.split(",")] for line in f]


def make_move(position, direction):
    moves = {
        "U": (1, 0),
        "D": (-1, 0),
        "R": (0, 1),
        "L": (0, -1)
    }
    return tuple(map(sum, zip(position, moves.get(direction))))


def get_points(wire):
    position = (0, 0)
    steps = 0
    points = {}
    for i in wire:
        for _ in range(int(i[1:])):
            steps += 1
            position = make_move(position, i[0])

            if position not in points:
                points[position] = steps

    return points


w1, w2 = read("input.txt")

points1 = get_points(w1)
points2 = get_points(w2)


def part_one():
    return min(abs(p1) + abs(p2) for p1, p2 in points1.keys() & points2.keys())


def part_two():
    return min(points1[p] + points2[p] for p in points1.keys() & points2.keys())
