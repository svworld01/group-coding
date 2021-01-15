# created by KUMAR SHANU

# 2. Isomorphic Strings
# https://leetcode.com/problems/isomorphic-strings

from collections import defaultdict


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # len of strings must be equal
        if len(s) != len(t):
            return False

        # create a hashmap of string
        hashmap = defaultdict(str)

        # replace chars of string
        for i in range(len(s)):
            if s[i] not in hashmap and t[i] not in hashmap.values():
                hashmap[s[i]] = t[i]

        # checking for isomorphic
        for i in range(len(s)):
            if hashmap[s[i]] != t[i]:
                return False
        return True
