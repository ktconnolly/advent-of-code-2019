import unittest

from day_6 import run


class TestDay6(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(145250, run.part_one())

    def test_part_two(self):
        self.assertEqual(274, run.part_two())


if __name__ == "__main__":
    unittest.main()
