# Created by KUMAR SHANU

# 1. Running Sum of 1d Array
# https://leetcode.com/problems/running-sum-of-1d-array/


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums
