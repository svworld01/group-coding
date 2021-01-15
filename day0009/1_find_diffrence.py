# created by KUMAR SHANU

# 1. Find the Difference
# https://leetcode.com/problems/find-the-difference/

# Solution 1
"""Using Sorting"""


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = sorted(s)
        t = sorted(t)
        i = 0
        while i < len(s):
            if s[i] != t[i]:
                return t[i]
            i += 1
        return t[-1]


# Solution 2
"""Using Hash"""

from collections import defaultdict


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        abcd = "abcdefghijklmnopqrstuvwxyz"
        s_count = defaultdict(int)
        t_count = defaultdict(int)
        for l in s:
            s_count[l] += 1

        for l in t:
            t_count[l] += 1
        print(s_count, t_count)
        for l in abcd:
            if s_count[l] != t_count[l]:
                return l
