from collections import namedtuple, defaultdict
import math

Point = namedtuple("Point", "x y")


def read(file):
    with open(file, "r") as f:
        return [
            Point(x, y) for y, line in enumerate(f.readlines())
            for x, c in enumerate(line) if c == '#'
        ]


def angle(p1, p2):
    return math.degrees(math.atan2(p1.y - p2.y, p1.x - p2.x))


def distance(p1, p2):
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)


def part_one():
    asteroids = read("input.txt")
    angles = defaultdict(set)

    for a1 in asteroids:
        for a2 in asteroids:
            if a1 == a2:
                continue

            angles[a1].add(angle(a1, a2))

    return len(max(angles.values(), key=len))


def part_two():
    pass
