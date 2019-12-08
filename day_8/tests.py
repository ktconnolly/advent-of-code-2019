import unittest

from day_8 import run


class TestDay8(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(2318, run.part_one())

    def test_part_two(self):
        pass


if __name__ == '__main__':
    unittest.main()
