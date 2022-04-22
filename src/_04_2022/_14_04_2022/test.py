import unittest

from src._04_2022._14_04_2022.first_last_index import Solution


class Test_Solution(unittest.TestCase):
    def test_first_last_index(self):
        self.assertEqual(
            Solution().getRange([1, 2, 2, 2, 2, 3, 4, 7, 8, 8], 2), [1, 4]
        )
        self.assertTrue(
            Solution().getRange([1, 2, 3, 4, 5, 6, 10], 9), [-1, -1]
        )
        self.assertTrue(
            Solution().getRange([100, 150, 150, 153], target=150), [1, 2]
        )
        self.assertTrue(
            Solution().getRange([1, 3, 3, 5, 7, 8, 9, 9, 9, 15], target=9),
            [6, 8],
        )


if __name__ == "__main__":
    unittest.main()
