import unittest

from day_11 import run


class TestDay11(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(1883, run.part_one())

    def test_part_two(self):
        result = [
            '  ##  ###  #  #  ##  #  # ###  #### #  #  ',
            ' #  # #  # #  # #  # #  # #  # #    #  #  ',
            ' #  # #  # #  # #    #  # #  # ###  ####  ',
            ' #### ###  #  # # ## #  # ###  #    #  #  ',
            ' #  # #    #  # #  # #  # # #  #    #  #  ',
            ' #  # #     ##   ###  ##  #  # #    #  #  '
        ]
        self.assertEqual(result, run.part_two())


if __name__ == "__main__":
    unittest.main()
