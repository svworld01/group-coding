# created by KUMAR SHANU

# 2. Count Negative Numbers in a Sorted Matrix
# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

## Solution 1
"""
Simple Brute Force Solution
"""


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        c = 0
        for nums in grid:
            for n in nums:
                if n < 0:
                    c += 1
        return c


## Solution 2


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        c = 0
        for nums in grid:
            for i in range(len(nums)):
                if nums[i] < 0:
                    c += len(nums) - i
                    break
        return c


## Solution 3
"""
Faster Solution
Binary Search based.
"""


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        i, j = 0, 0
        count = 0
        while i < m:

            if grid[i][j] < 0:
                count += n - j
                i += 1
                j = 0
            else:
                j += 1
            if j == n:
                j = 0
                i += 1
        return count


## Solution 4
"""
Fastest Solution
"""


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        i, j = m - 1, 0
        count = 0
        while i >= 0 and j < n:

            if grid[i][j] < 0:
                count += n - j
                i -= 1
            else:
                j += 1
        return count
