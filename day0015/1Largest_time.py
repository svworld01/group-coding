# created by KUMAR SHANU

# 1. Largest Time for Given Digits
# https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/554/week-1-september-1st-september-7th/3445/

from itertools import permutations


class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        ans = ''
        for p in permutations(A):
            if (p[0] * 10 + p[1] <= 23) and (p[2] * 10 + p[3]) <= 59:
                ans = max(ans,
                          str(p[0]) + str(p[1]) + ':' + str(p[2]) + str(p[3]))
        return ans
