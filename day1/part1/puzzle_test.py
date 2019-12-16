import unittest
import puzzle

class TestBasic(unittest.TestCase):
    def test_basic_parse(self):
        data = puzzle.parse('''+1
        +13
        +2'''.split())
        self.assertEqual([1, 13, 2], data)

    def test_basic_solve(self):
        data = [10, 10, 14]
        self.assertEqual(4, puzzle.solve(data))

    def test_pass(self):
        data = puzzle.parse(open(r"C:\Users\user\source\repos\advent-of-code-2019\day1\input.txt", "r").readlines())
        answer = puzzle.solve(data)
        self.assertEqual(3287620, answer)


if __name__ == '__main__':
    unittest.main()
