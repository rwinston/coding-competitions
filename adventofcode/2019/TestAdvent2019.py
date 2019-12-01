import unittest
from Advent2019 import Day1


class Day1TestCase(unittest.TestCase):
    def test_solve_part1(self):
        puzzle = Day1()
        answer = puzzle.solve_part1('data/day1.dat')
        self.assertEqual(3317100, answer)

    def test_solve_part2(self):
        puzzle = Day1()
        answer = puzzle.solve_part2('data/day1.dat')
        print(answer)

if __name__ == '__main__':
    unittest.main()
