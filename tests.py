import unittest

import day_01
import day_02
import day_03
import day_04
import day_05
import day_06
import day_07
import day_08
import day_09
import day_10
import day_11
import day_12
import day_13
import day_14
import day_15
import day_16


class Tests(unittest.TestCase):
    def test_day_01_part_one(self):
        self.assertEqual(3512133, day_01.part_one())

    def test_day_01_part_two(self):
        self.assertEqual(5265294, day_01.part_two())

    def test_day_02_part_one(self):
        self.assertEqual(4576384, day_02.part_one())

    def test_day_02_part_two(self):
        self.assertEqual(5398, day_02.part_two())

    def test_day_03_part_one(self):
        self.assertEqual(1626, day_03.part_one())

    def test_day_03_part_two(self):
        self.assertEqual(27330, day_03.part_two())

    def test_day_04_part_one(self):
        self.assertEqual(460, day_04.part_one())

    def test_day_04_part_two(self):
        self.assertEqual(290, day_04.part_two())

    def test_day_05_part_one(self):
        self.assertEqual(12234644, day_05.part_one())

    def test_day_05_part_two(self):
        self.assertEqual(3508186, day_05.part_two())

    def test_day_06_part_one(self):
        self.assertEqual(145250, day_06.part_one())

    def test_day_06_part_two(self):
        self.assertEqual(274, day_06.part_two())

    def test_day_07_part_one(self):
        self.assertEqual(255840, day_07.part_one())

    def test_day_07_part_two(self):
        self.assertEqual(84088865, day_07.part_two())

    def test_day_08_part_one(self):
        self.assertEqual(2318, day_08.part_one())

    def test_day_08_part_two(self):
        result = [
            " ##  #  # ####  ##  ###  ",
            "#  # #  # #    #  # #  # ",
            "#  # #### ###  #    ###  ",
            "#### #  # #    #    #  # ",
            "#  # #  # #    #  # #  # ",
            "#  # #  # #     ##  ###  ",
        ]
        self.assertEqual(result, day_08.part_two())

    def test_day_09_part_one(self):
        self.assertEqual(2457252183, day_09.part_one())

    def test_day_09_part_two(self):
        self.assertEqual(70634, day_09.part_two())

    def test_day_10_part_one(self):
        self.assertEqual(278, day_10.part_one())

    def test_day_10_part_two(self):
        self.assertEqual(1417, day_10.part_two())

    def test_day_11_part_one(self):
        self.assertEqual(1883, day_11.part_one())

    def test_day_11_part_two(self):
        result = [
            '  ##  ###  #  #  ##  #  # ###  #### #  #  ',
            ' #  # #  # #  # #  # #  # #  # #    #  #  ',
            ' #  # #  # #  # #    #  # #  # ###  ####  ',
            ' #### ###  #  # # ## #  # ###  #    #  #  ',
            ' #  # #    #  # #  # #  # # #  #    #  #  ',
            ' #  # #     ##   ###  ##  #  # #    #  #  '
        ]
        self.assertEqual(result, day_11.part_two())

    def test_day_12_part_one(self):
        self.assertEqual(10028, day_12.part_one())

    def test_day_12_part_two(self):
        self.assertEqual(314610635824376, day_12.part_two())

    def test_day_13_part_one(self):
        self.assertEqual(432, day_13.part_one())

    def test_day_13_part_two(self):
        self.assertEqual(22225, day_13.part_two())

    def test_day_14_part_one(self):
        self.assertEqual(378929, day_14.part_one())

    def test_day_14_part_two(self):
        self.assertEqual(3445249, day_14.part_two())

    def test_day_15_part_one(self):
        self.assertEqual(216, day_15.part_one())

    def test_day_15_part_two(self):
        self.assertEqual(326, day_15.part_two())

    def test_day_16_part_one(self):
        self.assertEqual('30379585', day_16.part_one())


if __name__ == "__main__":
    unittest.main()
