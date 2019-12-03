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


def get_points(wire):
    current = (0, 0)
    points = set()

    for i in wire:
        for _ in range(int(i[1:])):
            current = make_move(current, i[0])
            points.add(current)

    return points


def get_steps(wire, target):
    current = (0, 0)
    steps = 0
    for i in wire:
        for _ in range(int(i[1:])):
            if current == target:
                return steps

            current = make_move(current, i[0])
            steps += 1


def get_min_distance(points1, points2):
    return min(abs(p1) + abs(p2) for p1, p2 in points1.intersection(points2))


def part_one():
    wire1 = read("input.txt")[0]
    wire2 = read("input.txt")[1]

    points1 = get_points(wire1)
    points2 = get_points(wire2)

    return get_min_distance(points1, points2)


def part_two():
    wire1 = read("input.txt")[0]
    wire2 = read("input.txt")[1]

    points1 = get_points(wire1)
    points2 = get_points(wire2)

    return min(
        get_steps(wire1, p) + get_steps(wire2, p)
        for p in points1.intersection(points2)
    )
