import unittest

from day_15 import run


class TestDay15(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(216, run.part_one())

    def test_part_two(self):
        self.assertEqual(326, run.part_two())


if __name__ == "__main__":
    unittest.main()
