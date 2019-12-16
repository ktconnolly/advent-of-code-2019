from collections import defaultdict
from math import ceil


def get_chems(reaction):
    chems = []
    for chem in reaction.split(", "):
        amount, chem = chem.split()
        chems.append((int(amount), chem))
    return chems


def read(file):
    reactions = {}
    with open(file) as f:
        for line in f:
            reaction, product = line.strip().split(" => ")
            amount, chem = product.split()
            reactions[chem] = (int(amount), get_chems(reaction))

    return reactions


def get_ore(reactions, chem="FUEL", amount=1, excess=None):
    if chem == "ORE":
        return amount

    if excess is None:
        excess = defaultdict(int)

    if amount <= excess[chem]:
        excess[chem] -= amount
        amount = 0
    else:
        amount -= excess[chem]
        excess[chem] = 0

    produced, inputs = reactions[chem]
    n = ceil(amount / produced)

    ore = 0
    for required, input_chem in inputs:
        ore += get_ore(reactions, input_chem, n * required, excess)

    excess[chem] += n * produced - amount

    return ore


def maximum_fuel(reactions, available_ore):
    lower = 0
    upper = available_ore

    while lower + 1 < upper:
        mid = (lower + upper) // 2
        ore = get_ore(reactions, amount=mid)

        if ore > available_ore:
            upper = mid
        elif ore < available_ore:
            lower = mid
        else:
            return ore

    return lower


def part_one():
    reactions = read("inputs/day_14.txt")
    return get_ore(reactions)


def part_two():
    reactions = read("inputs/day_14.txt")
    return maximum_fuel(reactions, 1000000000000)
