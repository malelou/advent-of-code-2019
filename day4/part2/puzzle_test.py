import unittest
import puzzle

class TestBasic(unittest.TestCase):
    def test_basic_solve(self):
        self.assertEqual(1, puzzle.solve([123453, 123465]))

    def test_pass(self):
        self.assertEqual(945, puzzle.solve([264360, 746325]))


if __name__ == '__main__':
    unittest.main()
