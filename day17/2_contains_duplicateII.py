# created by KUMAR SHANU

# 2. Contains Duplicate II
# https://leetcode.com/problems/contains-duplicate-ii

from collections import defaultdict


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # hash
        d = defaultdict(list)

        # store all index of the number
        for idx, val in enumerate(nums):
            d[val].append(idx)

        for i in d:
            for j in range(1, len(d[i])):
                if d[i][j] - d[i][j - 1] <= k:
                    return True
        return False
