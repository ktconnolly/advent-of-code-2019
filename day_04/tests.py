import unittest

from day_04 import run


class TestDay4(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(460, run.part_one())

    def test_part_two(self):
        self.assertEqual(290, run.part_two())


if __name__ == "__main__":
    unittest.main()
