def read(file):
    with open(file, "r") as f:
        return [l.strip().split(")") for l in f]


def get_parents(child, orbits):
    p = orbits.get(child)

    if not p:
        return []

    return [p] + get_parents(p, orbits)


def part_one():
    orbits = {c: p for p, c in read("input.txt")}
    return sum(len(get_parents(obj, orbits)) for obj in orbits.keys())


def part_two():
    orbits = {c: p for p, c in read("input.txt")}

    you_parents = get_parents("YOU", orbits)
    santa_parents = get_parents("SAN", orbits)

    for p in you_parents:
        if p in santa_parents:
            return you_parents.index(p) + santa_parents.index(p)
