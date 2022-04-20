import unittest

from _19_04_2022.non_decreasing import check


class TestSolution(unittest.TestCase):
    def test_non_decreasing(self):
        self.assertTrue(check([13, 4, 7]))
        self.assertFalse(check([5, 1, 3, 2, 5]))
