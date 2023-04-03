class Solution(object):
    """
    https://leetcode.com/problems/running-sum-of-1d-array/
    """

    def runningSum(self, nums):
        acc = 0
        result = []
        for num in nums:
            acc += num
            result.append(acc)
        return result
