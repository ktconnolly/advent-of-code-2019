import unittest

from day_12 import run


class TestDay12(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(run.part_one(), 10028)

    def test_part_two(self):
        pass


if __name__ == "__main__":
    unittest.main()
