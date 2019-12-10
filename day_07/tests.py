import unittest

from day_7 import run


class TestDay7(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(255840, run.part_one())

    def test_part_two(self):
        self.assertEqual(84088865, run.part_two())


if __name__ == "__main__":
    unittest.main()
