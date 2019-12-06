import math
import re


class Day1:
    def solve_part1(self, datafile):
        fuel=0
        with open(datafile) as fp:
            for line in fp:
                fuel = fuel + self.calc_fuel(int(line))
        return fuel

    def solve_part2(self, datafile):
        fuel = 0
        with open(datafile) as fp:
            for line in fp:
                fuel += self.calc_total_fuel(int(line))
        return fuel

    def calc_fuel(self, mass):
        return math.floor(mass/3)-2

    def calc_total_fuel(self, mass):
        fuel = max(0, math.floor(mass / 3) - 2)
        if fuel == 0:
            return 0
        return fuel + self.calc_total_fuel(fuel)


class Day2:
    slots = []
    data = []

    def __init__(self, data):
        self.data = data.split(',')
        self.slots = [None] * len(self.data)
        self.reset()

    def reset(self):
        for i, x in enumerate(self.data):
            d = int(x)
            self.slots[i] = d

    def solve_part1(self):
        self.run_computer()

    def run_computer(self):
        commands = self.slots
        for i in range(0, len(commands), 4):
            cmd = commands[i]
            if cmd == 1:
                self.slots[commands[i + 3]] = self.slots[commands[i + 1]] + self.slots[commands[i + 2]]
            elif cmd == 2:
                self.slots[commands[i + 3]] = self.slots[commands[i + 1]] * self.slots[commands[i + 2]]
            elif cmd == 99:
                break

    def get_state(self, i):
        return self.slots[i]

    def set_state(self, i, x):
        self.slots[i] = x


class Day3:
    ops = {}
    origin = []

    def __init__(self):
        self.ops['U'] = lambda: (-1, 0)
        self.ops['D'] = lambda: (1, 0)
        self.ops['L'] = lambda: (0, -1)
        self.ops['R'] = lambda: (0, 1)

    def add_point(self, t1, t2):
        return tuple(x + y for x, y in zip(t1,t2()))

    def manhattan(self, x):
        return int(math.fabs(x[0])+math.fabs(x[1]))

    def solve_part1(self, data):
        wires = []
        for line in data:
            wires.append(line)

        self.origin = (0,0)
        wire1_p = set()
        wire2_p = set()
        positions = [wire1_p, wire2_p]
        for i, wire in enumerate(wires):
            wire_pos = self.origin
            commands = wire.split(',')
            for cmd in commands:
                op = cmd[0]
                distance = int(cmd[1:])
                while distance > 0:
                    wire_pos = self.add_point(wire_pos, self.ops[op])
                    positions[i].add(wire_pos)
                    distance -= 1
        return list(map(self.manhattan, positions[0].intersection(positions[1])))

    def solve_part2(self, data):
        wires = []
        for line in data:
            wires.append(line)

        self.origin = (0, 0)
        wire1_p = {}
        wire2_p = {}
        steps = 0
        positions = [wire1_p, wire2_p]
        for i, wire in enumerate(wires):
            wire_pos = self.origin
            commands = wire.split(',')
            for cmd in commands:
                op = cmd[0]
                distance = int(cmd[1:])
                while distance > 0:
                    wire_pos = self.add_point(wire_pos, self.ops[op])
                    distance -= 1
                    steps += 1
                    positions[i][wire_pos] = steps
        points = list(set(positions[0].values()).intersection(set(positions[1].values())))
        return points


class Day4:
    def check(self, x):
        n = x

        b1 = True
        b2 = False

        while n > 10:
            digit = int(n % 10)
            prevdigit  = int((n/10) % 10)
            if prevdigit > digit:
                b1 = False
            if prevdigit == digit:
                b2 = True
            n /= 10

        return b1 & b2

    def check_partb(self, x):
        n = x

        b1 = True
        b2 = False

        runs = []
        current_run = 0
        while n > 10:
            digit = int(n % 10)
            prevdigit = int((n/10) % 10)

            if prevdigit > digit:
                b1 = False
            if digit == prevdigit:
                current_run += 1
            else:
                runs.append(current_run)
                current_run = 0
            n /= 10
        runs.append(current_run)
        return b1 & (1 in runs)

    def solve_part1(self, start , end):
        passes = 0
        for x in range(start, end+1):
            if self.check(x):
                passes += 1

        return passes

    def solve_part2(self, start , end):
        passes = 0
        for x in range(start, end+1):
            if self.check_partb(x):
                passes += 1

        return passes


class Day5:
    slots = []
    data = []

    def __init__(self, data):
        self.data = data.split(',')
        self.slots = [None] * len(self.data)
        self.reset()

    def reset(self):
        for i, x in enumerate(self.data):
            self.slots[i] = int(x)

    def solve_part1(self, inp):
        return self.run_computer(inp)

    def cmd_length(self, cmd):
        if cmd == 3 or cmd == 4:
            return 2
        elif cmd == 5 or cmd == 6:
            return 3
        else:
            return 4

    def get_param(self,x,immediate):
        if immediate == 1:
            return x
        else:
            return self.slots[x]

    def run_computer(self, inp):
        commands = self.slots
        out = ''
        i = 0
        while True:
            cmd = str(commands[i])
            op = int(cmd)
            inp_modes = [0, 0]

            print('{} : {}'.format(i, cmd))
            if len(cmd) >= 3:
                op = int(cmd[2:])
                inp_modes = [int(cmd[-3]), -0]
                if len(cmd) > 3:
                    inp_modes = [int(cmd[-3]), int(cmd[-4])]

            if op == 1:
                self.slots[int(commands[i + 3])] = self.get_param(int(commands[i + 1]), inp_modes[0]) + \
                                                   self.get_param(int(commands[i + 2]), inp_modes[1])
            elif op == 2:
                self.slots[int(commands[i + 3])] = self.get_param(int(commands[i + 1]), inp_modes[0]) * \
                                                   self.get_param(int(commands[i + 2]), inp_modes[1])
            elif op == 3:
                self.slots[int(commands[i + 1])] = inp
            elif op == 4:
                print(self.slots[int(commands[i + 1])])
                out = self.slots[int(commands[i + 1])]
            elif op == 5:
                if self.get_param(int(commands[i+1]), inp_modes[0]) != 0:
                    i = self.get_param(int(commands[i + 2]), inp_modes[1])
                    continue
            elif op == 6:
                if self.get_param(int(commands[i + 1]), inp_modes[0]) == 0:
                    i = self.get_param(int(commands[i + 2]), inp_modes[1])
                    continue
            elif op == 7:
                if self.get_param(int(commands[i + 1]), inp_modes[0]) < self.get_param(int(commands[i + 2]), inp_modes[1]):
                    self.slots[int(commands[i + 3])] = 1
                else:
                    self.slots[int(commands[i + 3])] = 0
            elif op == 8:
                if self.get_param(int(commands[i + 1]), inp_modes[0]) == self.get_param(int(commands[i + 2]), inp_modes[1]):
                    self.slots[int(commands[i + 3])] = 1
                else:
                    self.slots[int(commands[i + 3])] = 0
            elif op == 99:
                break
            else:
                print("Unrecognized command: {}".format(cmd))
            i += self.cmd_length(op)
        return out

    def get_state(self, i):
        return self.slots[i]

    def set_state(self, i, x):
        self.slots[i] = x


class Node:
    children = []
    parent = None
    name = ''

    def __init__(self, name, parent):
        self.name = name
        self.parent = parent

    def parent(self):
        return self.parent

    def add_orbit(self, node):
        self.children.append(node)

    def count_orbits(self):
        orbits = 0
        p = self.parent
        while p is not None:
            orbits += 1
            p = p.parent
        return orbits


class Day6:
    def solve(self, datafile):
        nodes = {}
        with open(datafile) as fp:
            for line in fp:
                (p, o) = line.split(')')
                child, parent = None

                if p in nodes:
                    parent = nodes[p]
                else:
                    parent = Node(p, None)

                if o in nodes:
                    child = nodes[o]
                else
                    child = Node(o, parent)

                if p in nodes:
                    nodes[p].add_orbit(o)

                node = Node(o, nodes[p])
                nodes[o] = node
        for node in nodes:
            print(node.count_orbits())
        return





