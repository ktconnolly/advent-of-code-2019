def read(file):
    with open(file, "r") as f:
        return [[i.strip() for i in line.split(",")] for line in f]


def make_move(position, direction):
    row, col = position

    if direction == "U":
        return row + 1, col
    elif direction == "D":
        return row - 1, col
    elif direction == "R":
        return row, col + 1
    elif direction == "L":
        return row, col - 1
    else:
        raise Exception(f"Invalid direction: {direction}")


def get_points(wire):
    position = (0, 0)
    points = set()
    for i in wire:
        for _ in range(int(i[1:])):
            position = make_move(position, direction=i[0])
            points.add(position)

    return points


def get_steps(wire, target):
    position = (0, 0)
    steps = 0
    for i in wire:
        for _ in range(int(i[1:])):
            if position == target:
                return steps

            position = make_move(position, direction=i[0])
            steps += 1


w1, w2 = read("input.txt")

points1 = get_points(w1)
points2 = get_points(w2)


def part_one():
    return min(abs(p1) + abs(p2) for p1, p2 in points1.intersection(points2))


def part_two():
    return min(
        get_steps(w1, p) + get_steps(w2, p)
        for p in points1.intersection(points2)
    )
