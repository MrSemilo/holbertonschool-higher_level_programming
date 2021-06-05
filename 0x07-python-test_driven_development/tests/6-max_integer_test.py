#!/usr/bin/python3
""" Unittest for max_integer([..]) """


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMax_integer(unittest.TestCase):
    """class to  add testing"""

    def test_Max_Integer(self):
        """correct cases"""

        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([4, 5, -6]), 5)
        self.assertEqual(max_integer([4 + 4, 5, 6]), 8)
        self.assertEqual(max_integer([1 * 2, 3, 4]), 4)
        self.assertEqual(max_integer([-5, -10, -20, -30]), -5)
        self.assertEqual(max_integer([4]), 4)

        """incorrect cases"""

        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1]), 1)

        self.assertIsInstance(max_integer([1, 2, 3]), int)
        self.assertIsInstance(max_integer([1.5, 2.5, 3.5]), float)

        self.assertRaises(TypeError, max_integer, ["hello", 1, 2, 3])
