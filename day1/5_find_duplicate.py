# created by KUMAR SHANU

# 5. Find the Duplicate Number
# https://leetcode.com/problems/find-the-duplicate-number/

## Solution 1
"""
In this solution we use Counter object to store count of
each element to a dictionary.
"""

from collections import Counter


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        cnt = Counter()
        for n in nums:
            cnt[n] += 1
        for i in cnt:
            if cnt[i] > 1:
                return i


## Solution 2
"""
In this solution we mark the values as negative by A[x] = -A[x].
And check if a value is already marked as negative, we found the duplicate
value.
Some algorithm use A[x] = str(A[x]), and check for datatype.
"""


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            x = abs(nums[i])
            if nums[x] < 0:
                return x
            nums[x] *= -1
