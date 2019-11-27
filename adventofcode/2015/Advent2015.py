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

    def nicer(self,s):
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
