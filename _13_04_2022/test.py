import unittest

from _13_04_2022.valid_parenthesis import Solution


class Test_Solution(unittest.TestCase):
    def test_valid_parenthesis(self):
        self.assertFalse(Solution().isValid("()(){(())"))
        self.assertTrue(Solution().isValid(""))
        self.assertTrue(Solution().isValid("([{}])()"))


if __name__ == "__main__":
    unittest.main()
