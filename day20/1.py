# created by KUMAR SHANU

# 1. Is Subsequence
# https://leetcode.com/problems/is-subsequence


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)


if __name__ == "__main__":
    print(Solution().isSubsequence('abc', "ahbgdc"))
