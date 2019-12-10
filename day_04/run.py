from collections import Counter


def get_passwords():
    for p in range(382345, 843167):
        yield str(p)


def is_ascending(p):
    return "".join(sorted(p)) == p


def consecutive_counts(p):
    return Counter(p).values()


def part_one():
    return sum(
        is_ascending(p) and max(consecutive_counts(p)) > 1
        for p in get_passwords()
    )


def part_two():
    return sum(
        is_ascending(p) and 2 in consecutive_counts(p)
        for p in get_passwords()
    )
