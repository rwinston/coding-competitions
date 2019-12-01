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
