# created by KUMAR SHANU
# 1. Valid Perfect Square
# https://leetcode.com/problems/valid-perfect-square/

## Solution 1
"""Simple Solution"""


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for n in range(1, ceil(sqrt(num)) + 1):
            if n * n == num:
                return True
        return False


## Solution 2
"""Optimal Solution using Binary Search"""


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num is 1:
            return True
        l, r = 1, num
        while l <= r:
            mid = (l + r) // 2
            if mid * mid == num:
                return True
            elif mid * mid > num:
                r = mid - 1
            else:
                l = mid + 1
        return False
