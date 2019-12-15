WALL = 0
SUCCESSFUL_MOVE = 1
OXYGEN = 2

NORTH = 1
SOUTH = 2
WEST = 3
EAST = 4


def read(file):
    with open(file, "r") as f:
        return [int(i) for i in f.readline().split(",")]


class Computer:
    def __init__(self, code):
        self.code = code.copy()
        self.ptr = 0
        self.relative_base = 0
        self.inputs = []

    def add_input(self, inp):
        self.inputs.append(inp)

    def get_opcode(self):
        return self.code[self.ptr] % 100

    def get_mode(self, n):
        return self.code[self.ptr] // (10 ** (1 + n)) % 10

    def get_param(self, param_num):
        mode = self.get_mode(param_num)
        index = self.code[self.ptr + param_num]

        if mode == 0:
            return self.read(index)
        elif mode == 1:
            return index
        elif mode == 2:
            return self.read(index + self.relative_base)
        else:
            raise Exception("Invalid mode")

    def set_param(self, param_num, val):
        mode = self.get_mode(param_num)
        index = self.code[self.ptr + param_num]

        if mode == 0:
            self.write(index, val)
        elif mode == 2:
            self.write(index + self.relative_base, val)
        else:
            raise Exception("Invalid mode")

    def read(self, index):
        if index > len(self.code) - 1:
            self.resize(index)

        return self.code[index]

    def write(self, index, val):
        if index > len(self.code) - 1:
            self.resize(index)

        self.code[index] = val

    def resize(self, index):
        self.code += [0 for _ in range(index - len(self.code) + 1)]

    def run(self):
        while self.ptr < len(self.code):
            op = self.get_opcode()
            if op == 99:
                break

            if op == 1:
                self.set_param(3, self.get_param(1) + self.get_param(2))
                self.ptr += 4
            elif op == 2:
                self.set_param(3, self.get_param(1) * self.get_param(2))
                self.ptr += 4
            elif op == 3:
                self.set_param(1, self.inputs.pop())
                self.ptr += 2
            elif op == 4:
                out = self.get_param(1)
                self.ptr += 2
                return out
            elif op == 5:
                self.ptr = self.get_param(2) if self.get_param(1) != 0 else self.ptr + 3
            elif op == 6:
                self.ptr = self.get_param(2) if self.get_param(1) == 0 else self.ptr + 3
            elif op == 7:
                self.set_param(3, int(self.get_param(1) < self.get_param(2)))
                self.ptr += 4
            elif op == 8:
                self.set_param(3, int(self.get_param(1) == self.get_param(2)))
                self.ptr += 4
            elif op == 9:
                self.relative_base += self.get_param(1)
                self.ptr += 2
            else:
                raise Exception("Invalid opcode")


def get_opposite(move):
    return {NORTH: SOUTH, SOUTH: NORTH, WEST: EAST, EAST: WEST}.get(move)


def make_move(position, direction):
    moves = {NORTH: (0, 1), SOUTH: (0, -1), WEST: (-1, 0), EAST: (1, 0)}
    return tuple(map(sum, zip(position, moves.get(direction))))


def get_neighbours(pos):
    return [make_move(pos, direction) for direction in range(1, 5)]


def get_ship_map():
    robot = Computer(read("input.txt"))
    pos = (0, 0)
    ship_map = {}
    moves = []

    # contains directions (value) we haven't attempted for each
    # coordinate (key)
    unexplored = {}

    while True:
        ship_map[pos] = SUCCESSFUL_MOVE

        if pos not in unexplored:
            unexplored[pos] = [1, 2, 3, 4]

        if unexplored[pos]:
            back_tracking = False
            move = unexplored[pos].pop()
        else:
            back_tracking = True
            prev = moves.pop()
            move = get_opposite(prev)

        robot.add_input(move)
        status = robot.run()

        if status == SUCCESSFUL_MOVE:
            pos = make_move(pos, move)

            if not back_tracking:
                moves.append(move)

        elif status == OXYGEN:
            ship_map[pos] = OXYGEN
            return ship_map


def bfs(graph, start, target):
    queue = [[start]]
    visited = set()

    while queue:
        path = queue.pop(0)
        vertex = path[-1]

        if graph.get(vertex) == target or vertex == target:
            return len(path)

        if vertex in visited:
            continue

        visited.add(vertex)
        for neighbour in get_neighbours(vertex):
            if graph.get(vertex, 0) == 1:
                new_path = path.copy()
                new_path.append(neighbour)
                queue.append(new_path)


def part_one():
    ship = get_ship_map()
    return bfs(ship, start=(0, 0), target=OXYGEN)


def part_two():
    ship = get_ship_map()
    oxygen_location = None

    for coordinate in ship:
        if ship[coordinate] == OXYGEN:
            oxygen_location = coordinate

    return max(bfs(ship, coordinate, oxygen_location) for coordinate in ship)
