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

