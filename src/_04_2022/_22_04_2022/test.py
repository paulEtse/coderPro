import unittest

from src._04_2022._22_04_2022.maxStack import MaxStack


class TestSolution(unittest.TestCase):
    def test_max_stack(self):
        s = MaxStack()
        s.push(1)
        s.push(2)
        s.push(3)
        s.push(2)
        self.assertTrue(s.max(), 3)
        s.pop()
        s.pop()
        self.assertTrue(s.max(), 2)
