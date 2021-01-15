# created by KUMAR SHANU

# 2. Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # base case
        if len(strs) is 0:
            return ""

        # sort the array
        strs = sorted(strs)
        first = strs[0]
        last = strs[len(strs) - 1]

        # because array is sorted only compare first and last string
        i = 0
        while i < len(first):
            if first[i] == last[i]:
                i += 1
            else:
                break

        # return the part of first string which is common in last sting
        return "" if i == 0 else first[0:i]
