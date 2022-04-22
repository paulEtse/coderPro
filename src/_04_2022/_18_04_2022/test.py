import unittest

from src._04_2022._18_04_2022.single_number import (
    single_number,
    single_number__o_n_space,
)


class TestSolution(unittest.TestCase):
    def test_non_decreasing(self):
        self.assertEqual(single_number([4, 3, 2, 4, 1, 3, 2]), 1)

    def test_non_decreasing__o_n_space(self):
        self.assertEqual(single_number__o_n_space([4, 3, 2, 4, 1, 3, 2]), 1)
