import re
import copy


def read(file):
    with open(file, "r") as f:
        return [list(map(int, re.findall(r'[-\d]+', l))) for l in f]


class Moon:
    def __init__(self, x, y, z):
        self.pos = {"x": x, "y": y, "z": z}
        self.vel = {"x": 0, "y": 0, "z": 0}

    def update_position(self):
        for key in self.pos:
            self.pos[key] += self.vel[key]

    def energy(self):
        pot = map(abs, self.pos.values())
        kin = map(abs, self.vel.values())
        return sum(pot) * sum(kin)


def update(moons):
    new_moons = [copy.deepcopy(m) for m in moons]

    for i, m1 in enumerate(moons):
        for j, m2 in enumerate(moons[i + 1:], i + 1):

            for c in "xyz":
                if m1.pos[c] < m2.pos[c]:
                    new_moons[i].vel[c] += 1
                    new_moons[j].vel[c] -= 1
                elif m1.pos[c] > m2.pos[c]:
                    new_moons[i].vel[c] -= 1
                    new_moons[j].vel[c] += 1

    for m in new_moons:
        m.update_position()

    return new_moons


def part_one():
    moons = [Moon(*pos) for pos in read("input.txt")]
    for _ in range(1000):
        moons = update(moons)

    return sum(m.energy() for m in moons)


def part_two():
    pass
