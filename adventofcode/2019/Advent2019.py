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
    grid = []
    wires = []
    ops = {}
    origin = []

    def __init__(self, data, size):
        self.grid = [x[:] for x in [[0] * size] * size]

        for line in data:
            self.wires.append(line)

        self.ops['U'] = lambda: (-1, 0)
        self.ops['D'] = lambda: (1, 0)
        self.ops['L'] = lambda: (0, -1)
        self.ops['R'] = lambda: (0, 1)

    def add_point(self, t1, t2):
        return tuple(lambda x, y: x + y, t1, t2)

    def manhattan(self, t1):
        return math.fabs(t1[0])+math.fabs(t1[1])

    def solve_part1(self):
        self.origin = (0,0)
        wire1_p = wire2_p = set()
        positions = [wire1_p, wire2_p]
        for i, wire in enumerate(self.wires):
            wire_pos = self.origin
            print('starting position: {},{}'.format(wire_pos[0], wire_pos[1]))
            commands = wire.split(',')
            for cmd in commands:
                op = cmd[0]
                distance = int(cmd[1:])
                while distance > 0:
                    wire_pos = self.add_point(wire_pos, self.ops[op])
                    positions[i].add(wire_pos)
                    distance -= 1
        print(positions[0].intersection(positions[1]))
        return map(self.manhattan, positions[0].intersection(positions[1]))


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







