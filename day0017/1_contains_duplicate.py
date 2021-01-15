# created by KUMAR SHANU

# 1. Contains Duplicate
# https://leetcode.com/problems/contains-duplicate

# Solution 1
from collections import defaultdict


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = defaultdict(int)
        for n in nums:
            d[n] += 1

        for i in d:
            if d[i] > 1:
                return True
        return False


# Solution 2
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                return True
        return False


# Solution 3
# Python Oneliner
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) > len(set(nums))
