from collections import Counter


def is_ascending(p):
    return all(x <= y for x, y in zip(p, p[1:]))


def part_one():
    return sum(
        1 if is_ascending(str(p)) and max(Counter(str(p)).values()) > 1 else 0
        for p in range(382345, 843167)
    )


def part_two():
    return sum(
        1 if is_ascending(str(p)) and 2 in Counter(str(p)).values() else 0
        for p in range(382345, 843167)
    )
