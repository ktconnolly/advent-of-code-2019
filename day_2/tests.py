import unittest

from day_2 import run


class TestDay2(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(4576384, run.part_one())

    def test_part_two(self):
        self.assertEqual(5398, run.part_two())


if __name__ == '__main__':
    unittest.main()
