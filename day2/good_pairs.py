# created by KUMAR SHANU

# 1. Number of Good Pairs
# https://leetcode.com/problems/number-of-good-pairs/

from collections import Counter


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        cnt = Counter()
        for n in nums:
            cnt[n] += 1
        c = 0
        for n in cnt:
            c += cnt[n] * (cnt[n] - 1) // 2
        return c
