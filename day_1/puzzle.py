from utils import read_ints


def get_fuel(mass):
    return max(mass // 3 - 2, 0)


def get_total_fuel(mass):
    fuel = get_fuel(mass)

    if fuel == 0:
        return 0

    return fuel + get_total_fuel(fuel)


def part_one():
    return sum(get_fuel(mass) for mass in read_ints("input.txt"))


def part_two():
    return sum(get_total_fuel(mass)for mass in read_ints("input.txt"))
