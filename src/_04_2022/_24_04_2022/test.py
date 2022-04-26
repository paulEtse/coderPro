import unittest

from src._04_2022._24_04_2022.pythagorian_triplet import pythagoreanTriplets


class TestSolution(unittest.TestCase):
    def test_pythagorian_triplet(self):
        self.assertTrue(pythagoreanTriplets([3, 12, 5, 13]))
        self.assertFalse(pythagoreanTriplets([10, 4, 6, 12, 5]))
