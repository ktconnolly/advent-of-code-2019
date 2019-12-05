import unittest

from day_5 import run


class TestDay4(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(12234644, run.part_one())

    def test_part_two(self):
        self.assertEqual(3508186, run.part_two())


if __name__ == '__main__':
    unittest.main()
