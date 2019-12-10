import unittest

from day_10 import run


class TestDay10(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(278, run.part_one())

    def test_part_two(self):
        self.assertEqual(1417, run.part_two())


if __name__ == "__main__":
    unittest.main()
