class Solution(object):
    """
        https://leetcode.com/problems/find-pivot-index
    """
    def pivotIndex(self, nums):
        left = 0
        total = sum(nums)
        for pivot in range(len(nums)):
            if left == total-nums[pivot]-left:
                return pivot

            left += nums[pivot]
        return -1
