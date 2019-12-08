import unittest

from day_3 import run


class TestDay3(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(1626, run.part_one())

    def test_part_two(self):
        self.assertEqual(27330, run.part_two())


if __name__ == "__main__":
    unittest.main()
