import unittest

from day_14 import run


class TestDay14(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(378929, run.part_one())

    def test_part_two(self):
        self.assertEqual(3445249, run.part_two())


if __name__ == "__main__":
    unittest.main()
