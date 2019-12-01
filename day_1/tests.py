import unittest

from day_1 import puzzle


class TestDay1(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(3512133, puzzle.part_one())

    def test_part_two(self):
        self.assertEqual(5265294, puzzle.part_two())


if __name__ == '__main__':
    unittest.main()
