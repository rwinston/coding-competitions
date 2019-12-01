import functools
import hashlib
import re


class Day4:

    def __init__(self, seed):
        self.seed = seed

    def solve(self, n):
        nonce = 1
        while True:
            h = hashlib.md5(str(self.seed + str(nonce)).encode('utf-8')).hexdigest()
            if h.find('0' * n) == 0:
                return nonce
            nonce = nonce + 1


class Day5:
    def nice(self, s):
        return ((sum(map(lambda x: 1 if x in ['a', 'e', 'i', 'o', 'u'] else 0, s)) >= 3)
                and (re.search(r'([a-z])\1', s) is not None)
                and (re.search(r'(ab|cd|pq|xy)', s) is None))

    def nicer(self, s):
        return ((re.search(r'([a-z]{2}).*\1', s) is not None)
                and (re.search(r'([a-z])[a-z]\1', s) is not None))

    def solve_part1(self, datafile):
        count = 0
        with open(datafile) as fp:
            for line in fp:
                if self.nice(line):
                    count = count + 1
        return count

    def solve_part2(self, datafile):
        count = 0
        with open(datafile) as fp:
            for line in fp:
                if self.nicer(line):
                    count = count + 1
        return count


class Day6:
    grid = [[0 for x in range(1000)] for x in range(1000)]
    ops = {}

    def solve_part1(self, datafile):
        self.ops['turn on'] = lambda x: 1
        self.ops['turn off'] = lambda x: 0
        self.ops['toggle'] = lambda x: not (x)

        with open(datafile) as fp:
            for line in fp:
                self.process(line)
        return self.count_lights()

    def solve_part2(self, datafile):
        self.ops['turn on'] = lambda x: x + 1
        self.ops['turn off'] = lambda x: max(0, x - 1)
        self.ops['toggle'] = lambda x: x + 2

        with open(datafile) as fp:
            for line in fp:
                self.process(line)
        return self.count_lights()

    def process(self, line):
        m = re.match(r'(toggle|turn on|turn off) (\d+),(\d+) through (\d+),(\d+)$', line)
        if m:
            op = self.ops[m.group(1)]
            x1 = int(m.group(2))
            y1 = int(m.group(3))
            x2 = int(m.group(4))
            y2 = int(m.group(5))
            self.modify_grid(op, x1, y1, x2, y2)

    def modify_grid(self, op, x1, y1, x2, y2):
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                self.grid[i][j] = op(self.grid[i][j])

    def count_lights(self):
        count = 0
        for i in range(1000):
            for j in range(1000):
                count = count + self.grid[i][j]
        return count


class Day7:
    registers = {}
    fns = {}

    def __init__(self):
        self.fns['AND'] = lambda x, y: (x & y)
        self.fns['OR'] = lambda x, y: (x | y)
        self.fns['RSHIFT'] = lambda x, y: (x >> y)
        self.fns['LSHIFT'] = lambda x, y: (x << y)

    def solve_part1(self, datafile):
        with open(datafile) as fp:
            for line in fp:
                self.process(line)

    def solve_part2(self, datafile):
        with open(datafile) as fp:
            for line in fp:
                self.process(line)
        val = self.get_value('a')
        self.get_value.cache_clear()
        self.registers['b'] = str(val)
        return self.get_value('a') % 65536

    @functools.lru_cache()
    def get_value(self, k):
        try:
            return int(k)
        except ValueError:
            pass

        buffer = self.registers[k].split(" ")
        if "NOT" in buffer:
            return ~self.get_value(buffer[1]) % 65536
        if "AND" in buffer:
            return self.get_value(buffer[0]) & self.get_value(buffer[2]) % 65536
        elif "OR" in buffer:
            return self.get_value(buffer[0]) | self.get_value(buffer[2]) % 65536
        elif "LSHIFT" in buffer:
            return self.get_value(buffer[0]) << self.get_value(buffer[2]) % 65536
        elif "RSHIFT" in buffer:
            return self.get_value(buffer[0]) >> self.get_value(buffer[2]) % 65536
        else:
            return self.get_value(buffer[0])

    def process(self, line):
        print(line)
        (op, reg) = line.split("->")
        self.registers[reg.strip()] = op
