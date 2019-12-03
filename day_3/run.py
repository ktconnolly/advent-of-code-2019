def read(file):
    with open(file, "r") as f:
        return [[i.strip() for i in line.split(",")] for line in f]


def get_points(wire):
    current = (0, 0)
    points = set()

    for i in wire:
        for _ in range(int(i[1:])):
            row, col = current

            if i[0] == "U":
                current = (row + 1, col)
            elif i[0] == "D":
                current = (row - 1, col)
            elif i[0] == "R":
                current = (row, col + 1)
            elif i[0] == "L":
                current = (row, col - 1)

            points.add(current)

    return points


def get_steps(wire, point):
    current = (0, 0)
    steps = 0
    for i in wire:
        for _ in range(int(i[1:])):
            row, col = current

            if current == point:
                return steps

            if i[0] == "U":
                current = (row + 1, col)
            elif i[0] == "D":
                current = (row - 1, col)
            elif i[0] == "R":
                current = (row, col + 1)
            elif i[0] == "L":
                current = (row, col - 1)

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