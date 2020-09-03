# created by KUMAR SHANU

# 1. Valid Anagram
# https://leetcode.com/problems/valid-anagram


# Solution1
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sort first string
        s = sorted(s)

        #sort second string
        t = sorted(t)

        # if both are equal we found valid anagrams
        return s == t


# Solution2
from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # intializing hash
        d = defaultdict(int)

        # store the frequency of letters of first string in positives
        for l in s:
            d[l] += 1

        # store the frequency of letters of second string in negatives
        for l in t:
            d[l] -= 1

        # if frequency of letters is not equal to zero
        # return False
        for i in d:
            if d[i] != 0:
                return False
        return True
