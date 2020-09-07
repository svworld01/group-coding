# created by KUMAR SHANU

# 3. Contains Duplicate III
# https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/554/week-1-september-1st-september-7th/3446/

# Solution
"""
Solution using buckets and sliding window.
"""
from collections import OrderedDict


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int,
                                      t: int) -> bool:
        n = len(nums)

        # Edge Cases
        if n == 0 or k < 0 or t < 0:
            return False

        # initialize ordered map
        buckets = OrderedDict()

        for i, num in enumerate(nums):
            while len(buckets) > k:
                buckets.popitem(last=False)
            if (b := num // (t + 1)) in buckets:
                return True
            if b - 1 in buckets and abs(buckets[b - 1] - num) <= t:
                return True
            if b + 1 in buckets and abs(buckets[b + 1] - num) <= t:
                return True
            buckets[b] = nums[i]
        return False
