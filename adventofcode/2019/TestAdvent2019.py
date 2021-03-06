import unittest
from Advent2019 import Day1, Day2, Day3, Day4, Day5, Day6


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


class Day3TestCase(unittest.TestCase):
    def test_solve_simple(self):
        puzzle = Day3()
        distances = puzzle.solve_part1(['R8,U5,L5,D3','U7,R6,D4,L4'])
        self.assertEqual(2, len(distances))
        self.assertEqual(6, min(distances))

    def test_solve_simple2(self):
        puzzle = Day3()
        distances = puzzle.solve_part1(['R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51', 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'])
        self.assertEqual(135, min(distances))

    def test_solve_simple3(self):
        puzzle = Day3()
        distances = puzzle.solve_part1(['R75,D30,R83,U83,L12,D49,R71,U7,L72', 'U62,R66,U55,R34,D71,R55,D58,R83'])
        self.assertEqual(159, min(distances))

    def test_solve_part1(self):
        line1 = 'R1003,D138,L341,U798,L922,U153,R721,D177,L297,D559,L414,U470,L589,D179,L267,D954,R739,D414,L865,U688,R541,U242,R32,D607,L480,D401,L521,U727,L295,D154,R905,D54,L353,U840,L187,U942,R313,D143,R927,D962,R739,U152,R6,D9,L807,D67,R425,D235,L598,D107,L838,D522,L882,U780,L942,D29,R933,U129,L556,D11,L859,D455,L156,U673,L54,D141,R862,U88,R362,U742,L511,D408,R825,U622,R650,D393,L882,D969,R866,D232,L423,U371,L744,U35,L196,D189,R803,U663,R41,U741,R742,U929,L311,U30,R357,D776,L929,U85,R415,U540,R921,U599,R651,U79,R608,D620,L978,D92,L491,D310,L830,U656,R244,U72,L35,U768,R666,U356,R82,U596,L798,D455,L280,D626,R586,U668,R331,D245,L140,U3,R283,U813,R620,U975,L795,U477,L100,D94,R353,D732,R694,U702,L305,U497,R900,U810,L412,D954,R584,D444,L531,D875,R49,D328,L955,U227,L370,D548,L351,U571,R373,U743,R105,D226,L755,U325,R496,D960,L415,U262,R197,D508,R725,U930,L722,D162,L996,D610,R346,U680,L75,U211,R953,U147,R114,D48,L305,D284,L630,U575,R142,D518,R704,D820,L617,D118,R67,D674,L90,D916,L483,D598,L424,U92,R188,U413,L702,D262,R720,D995,L759,D732,L259,D814,L342,U642,L875,U726,R265,D143,R754,D235,L535,U1,R211,D720,R943,D726,L398,U636,R994,U653,L401,U877,R577,D460,L730,U889,R166,D641,L693,U490,L78,D80,R535,U551,L866,U283,L336,U586,L913,U474,R158,D220,R278,U11,R421,D661,R719,D696,R188,D735,L799,U391,R331,U581,R689,D82,R375,D125,R613,D705,L927,U18,R399,D352,L411,D777,L733,D884,R791,U973,R772,D878,R327,U215,L298,D360,R426,D872,L99,U78,L745,U59,L641,U73,L294,D247,R944,U512,L396'
        line2 = 'L1004,D252,L909,D935,R918,D981,L251,U486,R266,U613,L546,D815,L789,D692,L550,U633,R485,U955,R693,D784,R974,U529,R926,U550,L742,U88,R647,D572,R832,D345,R98,D122,R634,U943,L956,U551,R295,U122,L575,U378,R652,U97,R129,D872,R275,D492,L530,D328,R761,U738,R836,U884,R636,U776,L951,D977,R980,U526,L824,U125,R778,D818,R281,U929,R907,U234,L359,D521,R294,U137,L607,U421,L7,U582,R194,U979,L941,D999,R442,D330,L656,U410,R753,U704,R834,D61,R775,U750,R891,D989,R856,D944,R526,D44,R227,U938,R130,D280,L721,D171,R763,D677,L643,U931,L489,U250,L779,U552,R796,U220,R465,U700,L459,U766,R501,D16,R555,U257,R122,U452,L197,U905,L486,D726,L551,U487,R785,U470,L879,U149,L978,D708,R18,U211,L652,D141,L99,D190,L982,U556,R861,U745,L786,U674,R706,U986,R554,D39,R881,D626,R885,U907,R196,U532,L297,U232,L508,U283,L236,U613,L551,U647,R679,U760,L435,D475,R916,U669,R788,U922,R107,D503,R687,D282,L940,U835,L226,U421,L64,U245,R977,D958,L866,D328,R215,D532,R350,D199,R872,U373,R415,U463,L132,U225,L144,U786,R658,D535,R263,U263,R48,D420,L407,D177,L496,U521,R47,D356,L503,D557,R220,D879,L12,U853,R265,U983,L221,U235,R46,D906,L271,U448,L464,U258,R952,D976,L949,D526,L458,D753,L408,U222,R256,U885,R986,U622,R503,D5,L659,D553,R311,U783,L541,U17,R267,U767,L423,D501,R357,D160,L316,D912,R303,U648,L182,U342,L185,U743,L559,U816,R24,D203,R608,D370,R25,U883,L72,D816,L877,U990,R49,U331,L482,U37,L585,D327,R268,D106,L224,U401,L203,D734,L695,U910,L417,U105,R135,U876,L194,U723,L282,D966,R246,U447,R966,U346,L636,D9,L480,D35,R96'
        puzzle = Day3()
        distances = puzzle.solve_part1([line1, line2])
        print(min(distances))

    def test_solve_parts2_simple(self):
        puzzle = Day3()
        distances = puzzle.solve_part2(['R8,U5,L5,D3', 'U7,R6,D4,L4'])
        print(distances)


class Day4TestCase(unittest.TestCase):
    def test_solve_simple(self):
        puzzle = Day4()
        self.assertEqual(True, puzzle.check(111111))
        self.assertEqual(False, puzzle.check(223450))
        self.assertEqual(False, puzzle.check(123789))

        self.assertEqual(True, puzzle.check_partb(112233))
        self.assertEqual(False, puzzle.check_partb(123444))
        self.assertEqual(True, puzzle.check_partb(111122))
        self.assertEqual(True, puzzle.check_partb(112348))
        self.assertEqual(False, puzzle.check_partb(111238))

    def test_solve_part1(self):
        puzzle = Day4()
        print(puzzle.solve_part1(134564,585159))

    def test_solve_part2(self):
        puzzle = Day4()
        print(puzzle.solve_part2(134564,585159))


class Day5TestCase(unittest.TestCase):
    def test_solve_simple(self):
        puzzle = Day5('1002,4,3,4,33')
        puzzle.solve_part1(1)
        self.assertEqual(99, puzzle.get_state(4))

    def test_solve_simple2(self):
        puzzle = Day5('1101,100,-1,4,0')
        puzzle.solve_part1(1)
        self.assertEqual(99, puzzle.get_state(4))

    def test_solve_part1(self):
        data = '3, 225, 1, 225, 6, 6, 1100, 1, 238, 225, 104, 0, 1101, 82, 10, 225, 101, 94, 44, 224, 101, -165, 224, 224, 4, 224, 1002, 223, 8, 223, 101, 3, 224, 224, 1, 224, 223, 223, 1102, 35, 77, 225, 1102, 28, 71, 225, 1102, 16, 36, 225, 102, 51, 196, 224, 101, -3468, 224, 224, 4, 224, 102, 8, 223, 223, 1001, 224, 7, 224, 1, 223, 224, 223, 1001, 48, 21, 224, 101, -57, 224, 224, 4, 224, 1002, 223, 8, 223, 101, 6, 224, 224, 1, 223, 224, 223, 2, 188, 40, 224, 1001, 224, -5390, 224, 4, 224, 1002, 223, 8, 223, 101, 2, 224, 224, 1, 224, 223, 223, 1101, 9, 32, 224, 101, -41, 224, 224, 4, 224, 1002, 223, 8, 223, 1001, 224, 2, 224, 1, 223, 224, 223, 1102, 66, 70, 225, 1002, 191, 28, 224, 101, -868, 224, 224, 4, 224, 102, 8, 223, 223, 101, 5, 224, 224, 1, 224, 223, 223, 1, 14, 140, 224, 101, -80, 224, 224, 4, 224, 1002, 223, 8, 223, 101, 2, 224, 224, 1, 224, 223, 223, 1102, 79, 70, 225, 1101, 31, 65, 225, 1101, 11, 68, 225, 1102, 20, 32, 224, 101, -640, 224, 224, 4, 224, 1002, 223, 8, 223, 1001, 224, 5, 224, 1, 224, 223, 223, 4, 223, 99, 0, 0, 0, 677, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1105, 0, 99999, 1105, 227, 247, 1105, 1, 99999, 1005, 227, 99999, 1005, 0, 256, 1105, 1, 99999, 1106, 227, 99999, 1106, 0, 265, 1105, 1, 99999, 1006, 0, 99999, 1006, 227, 274, 1105, 1, 99999, 1105, 1, 280, 1105, 1, 99999, 1, 225, 225, 225, 1101, 294, 0, 0, 105, 1, 0, 1105, 1, 99999, 1106, 0, 300, 1105, 1, 99999, 1, 225, 225, 225, 1101, 314, 0, 0, 106, 0, 0, 1105, 1, 99999, 8, 226, 226, 224, 1002, 223, 2, 223, 1006, 224, 329, 101, 1, 223, 223, 1008, 677, 677, 224, 102, 2, 223, 223, 1006, 224, 344, 101, 1, 223, 223, 1107, 226, 677, 224, 102, 2, 223, 223, 1005, 224, 359, 101, 1, 223, 223, 1008, 226, 226, 224, 1002, 223, 2, 223, 1006, 224, 374, 1001, 223, 1, 223, 1108, 677, 226, 224, 1002, 223, 2, 223, 1006, 224, 389, 1001, 223, 1, 223, 7, 677, 226, 224, 1002, 223, 2, 223, 1006, 224, 404, 101, 1, 223, 223, 7, 226, 226, 224, 1002, 223, 2, 223, 1005, 224, 419, 101, 1, 223, 223, 8, 226, 677, 224, 1002, 223, 2, 223, 1006, 224, 434, 1001, 223, 1, 223, 7, 226, 677, 224, 1002, 223, 2, 223, 1006, 224, 449, 1001, 223, 1, 223, 107, 226, 677, 224, 1002, 223, 2, 223, 1005, 224, 464, 1001, 223, 1, 223, 1007, 677, 677, 224, 102, 2, 223, 223, 1005, 224, 479, 101, 1, 223, 223, 1007, 226, 226, 224, 102, 2, 223, 223, 1005, 224, 494, 1001, 223, 1, 223, 1108, 226, 677, 224, 102, 2, 223, 223, 1005, 224, 509, 101, 1, 223, 223, 1008, 677, 226, 224, 102, 2, 223, 223, 1005, 224, 524, 1001, 223, 1, 223, 1007, 677, 226, 224, 102, 2, 223, 223, 1005, 224, 539, 101, 1, 223, 223, 1108, 226, 226, 224, 1002, 223, 2, 223, 1005, 224, 554, 101, 1, 223, 223, 108, 226, 226, 224, 102, 2, 223, 223, 1005, 224, 569, 101, 1, 223, 223, 108, 677, 677, 224, 102, 2, 223, 223, 1005, 224, 584, 101, 1, 223, 223, 1107, 226, 226, 224, 1002, 223, 2, 223, 1006, 224, 599, 101, 1, 223, 223, 8, 677, 226, 224, 1002, 223, 2, 223, 1006, 224, 614, 1001, 223, 1, 223, 108, 677, 226, 224, 102, 2, 223, 223, 1006, 224, 629, 1001, 223, 1, 223, 1107, 677, 226, 224, 1002, 223, 2, 223, 1006, 224, 644, 1001, 223, 1, 223, 107, 677, 677, 224, 102, 2, 223, 223, 1005, 224, 659, 101, 1, 223, 223, 107, 226, 226, 224, 102, 2, 223, 223, 1006, 224, 674, 1001, 223, 1, 223, 4, 223, 99, 226'
        puzzle = Day5(data)
        output = puzzle.solve_part1(1)
        print(output)

    def test_solve_part2(self):
       data = '3, 225, 1, 225, 6, 6, 1100, 1, 238, 225, 104, 0, 1101, 82, 10, 225, 101, 94, 44, 224, 101, -165, 224, 224, 4, 224, 1002, 223, 8, 223, 101, 3, 224, 224, 1, 224, 223, 223, 1102, 35, 77, 225, 1102, 28, 71, 225, 1102, 16, 36, 225, 102, 51, 196, 224, 101, -3468, 224, 224, 4, 224, 102, 8, 223, 223, 1001, 224, 7, 224, 1, 223, 224, 223, 1001, 48, 21, 224, 101, -57, 224, 224, 4, 224, 1002, 223, 8, 223, 101, 6, 224, 224, 1, 223, 224, 223, 2, 188, 40, 224, 1001, 224, -5390, 224, 4, 224, 1002, 223, 8, 223, 101, 2, 224, 224, 1, 224, 223, 223, 1101, 9, 32, 224, 101, -41, 224, 224, 4, 224, 1002, 223, 8, 223, 1001, 224, 2, 224, 1, 223, 224, 223, 1102, 66, 70, 225, 1002, 191, 28, 224, 101, -868, 224, 224, 4, 224, 102, 8, 223, 223, 101, 5, 224, 224, 1, 224, 223, 223, 1, 14, 140, 224, 101, -80, 224, 224, 4, 224, 1002, 223, 8, 223, 101, 2, 224, 224, 1, 224, 223, 223, 1102, 79, 70, 225, 1101, 31, 65, 225, 1101, 11, 68, 225, 1102, 20, 32, 224, 101, -640, 224, 224, 4, 224, 1002, 223, 8, 223, 1001, 224, 5, 224, 1, 224, 223, 223, 4, 223, 99, 0, 0, 0, 677, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1105, 0, 99999, 1105, 227, 247, 1105, 1, 99999, 1005, 227, 99999, 1005, 0, 256, 1105, 1, 99999, 1106, 227, 99999, 1106, 0, 265, 1105, 1, 99999, 1006, 0, 99999, 1006, 227, 274, 1105, 1, 99999, 1105, 1, 280, 1105, 1, 99999, 1, 225, 225, 225, 1101, 294, 0, 0, 105, 1, 0, 1105, 1, 99999, 1106, 0, 300, 1105, 1, 99999, 1, 225, 225, 225, 1101, 314, 0, 0, 106, 0, 0, 1105, 1, 99999, 8, 226, 226, 224, 1002, 223, 2, 223, 1006, 224, 329, 101, 1, 223, 223, 1008, 677, 677, 224, 102, 2, 223, 223, 1006, 224, 344, 101, 1, 223, 223, 1107, 226, 677, 224, 102, 2, 223, 223, 1005, 224, 359, 101, 1, 223, 223, 1008, 226, 226, 224, 1002, 223, 2, 223, 1006, 224, 374, 1001, 223, 1, 223, 1108, 677, 226, 224, 1002, 223, 2, 223, 1006, 224, 389, 1001, 223, 1, 223, 7, 677, 226, 224, 1002, 223, 2, 223, 1006, 224, 404, 101, 1, 223, 223, 7, 226, 226, 224, 1002, 223, 2, 223, 1005, 224, 419, 101, 1, 223, 223, 8, 226, 677, 224, 1002, 223, 2, 223, 1006, 224, 434, 1001, 223, 1, 223, 7, 226, 677, 224, 1002, 223, 2, 223, 1006, 224, 449, 1001, 223, 1, 223, 107, 226, 677, 224, 1002, 223, 2, 223, 1005, 224, 464, 1001, 223, 1, 223, 1007, 677, 677, 224, 102, 2, 223, 223, 1005, 224, 479, 101, 1, 223, 223, 1007, 226, 226, 224, 102, 2, 223, 223, 1005, 224, 494, 1001, 223, 1, 223, 1108, 226, 677, 224, 102, 2, 223, 223, 1005, 224, 509, 101, 1, 223, 223, 1008, 677, 226, 224, 102, 2, 223, 223, 1005, 224, 524, 1001, 223, 1, 223, 1007, 677, 226, 224, 102, 2, 223, 223, 1005, 224, 539, 101, 1, 223, 223, 1108, 226, 226, 224, 1002, 223, 2, 223, 1005, 224, 554, 101, 1, 223, 223, 108, 226, 226, 224, 102, 2, 223, 223, 1005, 224, 569, 101, 1, 223, 223, 108, 677, 677, 224, 102, 2, 223, 223, 1005, 224, 584, 101, 1, 223, 223, 1107, 226, 226, 224, 1002, 223, 2, 223, 1006, 224, 599, 101, 1, 223, 223, 8, 677, 226, 224, 1002, 223, 2, 223, 1006, 224, 614, 1001, 223, 1, 223, 108, 677, 226, 224, 102, 2, 223, 223, 1006, 224, 629, 1001, 223, 1, 223, 1107, 677, 226, 224, 1002, 223, 2, 223, 1006, 224, 644, 1001, 223, 1, 223, 107, 677, 677, 224, 102, 2, 223, 223, 1005, 224, 659, 101, 1, 223, 223, 107, 226, 226, 224, 102, 2, 223, 223, 1006, 224, 674, 1001, 223, 1, 223, 4, 223, 99, 226'
       puzzle = Day5(data)
       output = puzzle.solve_part1(5)
       print(output)

    def test_compatible(self):
        puzzle = Day5('1,0,0,0,99')
        puzzle.solve_part1(0)
        self.assertEqual(puzzle.get_state(0), 2)

    def test_part2_examples(self):
        data = '3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8'
        puzzle = Day5(data)
        puzzle.solve_part1(8)

        data = '3,9,7,9,10,9,4,9,99,-1,8'
        puzzle = Day5(data)
        puzzle.solve_part1(3)

        data = '3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9'
        puzzle = Day5(data)
        puzzle.solve_part1(0)

        data = '3,3,1107,-1,8,3,4,3,99'
        puzzle = Day5(data)
        puzzle.solve_part1(8)

    def test_immediate(self):
        data = '3,3,1105,-1,9,1101,0,0,12,4,12,99,1'
        puzzle = Day5(data)
        puzzle.solve_part1(0)


class Day6TestCase(unittest.TestCase):
    def test_solve_simple(self):
        puzzle = Day6()
        puzzle.solve('data/day6.dat')
        self.assertEqual(99, puzzle.get_state(4))

if __name__ == '__main__':
    unittest.main()
