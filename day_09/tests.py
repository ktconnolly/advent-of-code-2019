import unittest

from day_9 import run


class TestDay9(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(2457252183, run.part_one())

    def test_part_two(self):
        self.assertEqual(70634, run.part_two())


if __name__ == "__main__":
    unittest.main()
