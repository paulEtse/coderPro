import unittest

from _11_04_2022.longuest_substring import Solution


class TestSolution(unittest.TestCase):
    def test_longuest_substring(self):
        Solution().lengthOfLongestSubstring("abrkaabcdefghijjxxx")
