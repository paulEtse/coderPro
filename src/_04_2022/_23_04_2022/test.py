import unittest

from src._04_2022._23_04_2022.climb_stairs import staircase


class TestSolution(unittest.TestCase):
    def test_climb_stairs(self):
        self.assertEqual(staircase(4), 5)
        self.assertEqual(staircase(5), 8)
