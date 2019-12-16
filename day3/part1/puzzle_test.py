import unittest
import puzzle

class TestBasic(unittest.TestCase):
    # def test_basic_parse(self):
    #     data = puzzle.parse(open(r"C:\Users\user\source\repos\advent-of-code-2019\day3\testinput.txt", "r").readlines())
    #     self.assertEqual([['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51'], ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']], data)

    def test_basic_solve(self):
        data = [['R2','U2'],['U2', 'R2']]
        self.assertEqual(4, puzzle.solve(data))

    def test_basic_solve2(self):
        data = [['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51'], ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']]
        self.assertEqual(135, puzzle.solve(data))

    def test_basic_solve3(self):
        data = [['R8','U5','L5','D3'], ['U7','R6','D4','L4']]
        self.assertEqual(6, puzzle.solve(data))

    def test_pass(self):
        data = puzzle.parse(open(r"C:\Users\user\source\repos\advent-of-code-2019\day3\input.txt", "r").readlines())
        answer = puzzle.solve(data)
        self.assertEqual(227, answer)


if __name__ == '__main__':
    unittest.main()
