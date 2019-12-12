import re
import copy


def read(file):
    with open(file, "r") as f:
        return [list(map(int, re.findall(r'[-\d]+', l))) for l in f]


class Moon:
    def __init__(self, x, y, z):
        self.pos = [x, y, z]
        self.vel = [0, 0, 0]

    def update_position(self):
        for i in range(3):
            self.pos[i] += self.vel[i]

    def energy(self):
        return sum(map(abs, self.pos)) * sum(map(abs, self.vel))

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


def update(moons):
    new_moons = [copy.deepcopy(m) for m in moons]

    for i, m1 in enumerate(moons):
        for j, m2 in enumerate(moons[i + 1:], i + 1):

            for c in range(3):
                if m1.pos[c] < m2.pos[c]:
                    new_moons[i].vel[c] += 1
                    new_moons[j].vel[c] -= 1
                elif m1.pos[c] > m2.pos[c]:
                    new_moons[i].vel[c] -= 1
                    new_moons[j].vel[c] += 1

    for m in new_moons:
        m.update_position()

    return new_moons


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b / gcd(a, b)


def part_one():
    moons = [Moon(*pos) for pos in read("input.txt")]
    for _ in range(1000):
        moons = update(moons)

    return sum(m.energy() for m in moons)


def part_two():
    moons = [Moon(*pos) for pos in read("input.txt")]
    initial_positions = [[m.pos[i] for m in moons] for i in range(3)]

    res = [0, 0, 0]
    count = 1
    while not all(res):
        moons = update(moons)
        poistions = [[m.pos[i] for m in moons] for i in range(3)]
        count += 1

        for i in range(3):
            if poistions[i] == initial_positions[i] and not res[i]:
                res[i] = count

    return int(lcm(lcm(res[0], res[1]), res[2]))
