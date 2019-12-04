from itertools import groupby


def get_passwords():
    for p in range(382345, 843167):
        yield str(p)


def is_ascending(p):
    return all(x <= y for x, y in zip(p, p[1:]))


def get_consecutive_counts(p):
    return list(len(list(y)) for x, y in groupby(p))


def part_one():
    return sum(
        1 if is_ascending(p) and max(get_consecutive_counts(p)) > 1 else 0
        for p in get_passwords()
    )


def part_two():
    return sum(
        1 if is_ascending(p) and 2 in (get_consecutive_counts(p)) else 0
        for p in get_passwords()
    )
