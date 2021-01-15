# created by KUMAR SHANU

# 2. K-diff Pairs in an Array
# https://leetcode.com/problems/k-diff-pairs-in-an-array/
"""Store frequency in dictionary"""
from collections import defaultdict


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        count = 0
        d = defaultdict(int)
        for num in nums:
            d[num] += 1

        for i in d:
            if k == 0 and d[i] > 1:
                count += 1
            elif k > 0 and ((i + k) in d):
                count += 1
        #print(d)
        return count
