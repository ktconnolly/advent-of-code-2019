import unittest

from day_13 import run


class TestDay13(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(432, run.part_one())

    def test_part_two(self):
        self.assertEqual(22225, run.part_two())


if __name__ == "__main__":
    unittest.main()
