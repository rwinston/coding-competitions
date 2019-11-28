import unittest
from Advent2015 import Day4,Day5,Day6


class Day4TestCase(unittest.TestCase):
    def test_solve(self):
        puzzle = Day4('abcdef')
        answer = puzzle.solve(5)
        self.assertEqual(609043, answer)

    def test_solve_part1(self):
        puzzle = Day4('bgvyzdsv')
        self.assertEqual(254575, puzzle.solve(5))

    def test_solve_part2(self):
        puzzle = Day4('bgvyzdsv')
        self.assertEqual(1038736, puzzle.solve(6))


class Day5TestCase(unittest.TestCase):
    def test_nice(self):
        puzzle = Day5()
        self.assertEqual(True, puzzle.nice('ugknbfddgicrmopn'))
        self.assertEqual(True, puzzle.nice('aaa'))
        self.assertEqual(False, puzzle.nice('jchzalrnumimnmhp'))
        self.assertEqual(False, puzzle.nice('haegwjzuvuyypxyu'))
        self.assertEqual(False, puzzle.nice('dvszwmarrgswjxmb'))

    def test_nicer(self):
        puzzle = Day5()
        self.assertEqual(True, puzzle.nicer('qjhvhtzxzqqjkmpb'))
        self.assertEqual(True, puzzle.nicer('xxyxx'))
        self.assertEqual(False, puzzle.nicer('uurcxstgmygtbstg'))
        self.assertEqual(False, puzzle.nicer('ieodomkazucvgmuy'))


    def test_part1(self):
        puzzle = Day5()
        print(puzzle.solve_part1('data/day5.dat'))

    def test_part2(self):
        puzzle = Day5()
        print(puzzle.solve_part2('data/day5.dat'))


class Day6TestCase(unittest.TestCase):
    def test_part1(self):
        puzzle = Day6()
        print(puzzle.solve_part1('data/day6.dat'))

    def test_modify(self):
        puzzle = Day6()
        puzzle.modify_grid(lambda x:x+2,0,0,999,999)
        self.assertEqual(2000000, puzzle.count_lights())

    def test_part2(self):
        puzzle = Day6()
        print(puzzle.solve_part2('data/day6.dat'))


if __name__ == '__main__':
    unittest.main()
