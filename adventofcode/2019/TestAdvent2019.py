import unittest
from Advent2019 import Day1, Day2


class Day1TestCase(unittest.TestCase):
    def test_solve_part1(self):
        puzzle = Day1()
        answer = puzzle.solve_part1('data/day1.dat')
        self.assertEqual(3317100, answer)

    def test_solve_part2(self):
        puzzle = Day1()
        answer = puzzle.solve_part2('data/day1.dat')
        print(answer)


class Day2TestCase(unittest.TestCase):
    def test_solve_examples(self):
        puzzle = Day2('1,0,0,0,99')
        puzzle.solve_part1()
        self.assertListEqual(puzzle.get_state(), [2, 0, 0, 0, 99])

    def test_solve_part1(self):
        data = '1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,9,19,1,13,19,23,2,23,9,27,1,6,27,31,2,10,31,35,1,6,35,39,2,9,39,' \
               '43,1,5,43,47,2,47,13,51,2,51,10,55,1,55,5,59,1,59,9,63,1,63,9,67,2,6,67,71,1,5,71,75,1,75,6,79,1,6,' \
               '79,83,1,83,9,87,2,87,10,91,2,91,10,95,1,95,5,99,1,99,13,103,2,103,9,107,1,6,107,111,1,111,5,115,1,' \
               '115,2,119,1,5,119,0,99,2,0,14,0'
        puzzle = Day2(data)
        puzzle.set_state(1, 12)
        puzzle.set_state(2, 2)
        puzzle.run_computer()
        print(puzzle.get_state())

    def test_solve_part2(self):
        data = '1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,9,19,1,13,19,23,2,23,9,27,1,6,27,31,2,10,31,35,1,6,35,39,2,9,39,' \
               '43,1,5,43,47,2,47,13,51,2,51,10,55,1,55,5,59,1,59,9,63,1,63,9,67,2,6,67,71,1,5,71,75,1,75,6,79,1,6,' \
               '79,83,1,83,9,87,2,87,10,91,2,91,10,95,1,95,5,99,1,99,13,103,2,103,9,107,1,6,107,111,1,111,5,115,1,' \
               '115,2,119,1,5,119,0,99,2,0,14,0'
        puzzle = Day2(data)
        for verb in range(100):
            for noun in range(100):
                puzzle.reset()
                puzzle.set_state(1, noun)
                puzzle.set_state(2, verb)
                puzzle.run_computer()
                if puzzle.get_state(0) == 19690720:
                    print(100*noun + verb)




if __name__ == '__main__':
    unittest.main()
