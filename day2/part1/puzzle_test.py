import unittest
import puzzle

class TestBasic(unittest.TestCase):
    def test_basic_solve(self):
        data = [1,0,0,0,99]
        self.assertEqual([2,0,0,0,99], puzzle.solve(data))

    def test_basic_solve2(self):
        data = [2,4,4,5,99,0]
        self.assertEqual([2,4,4,5,99,9801], puzzle.solve(data))
    
    def test_basic_solve3(self):
        data = puzzle.parse(open(r"C:\Users\user\source\repos\advent-of-code-2019\day2\testinput.txt", "r").readlines())
        self.assertEqual([30,1,1,4,2,5,6,0,99], puzzle.solve(data))

    def test_pass(self):
        data = puzzle.parse(open(r"C:\Users\user\source\repos\advent-of-code-2019\day2\input.txt", "r").readlines())
        answer = puzzle.solve(data)[0]
        self.assertEqual(4462686, answer)
 

if __name__ == '__main__':
    unittest.main()
