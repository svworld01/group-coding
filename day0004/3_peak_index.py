# created by KUMAR SHANU

# 3. Peak Index in a Mountain Array
# https://leetcode.com/problems/peak-index-in-a-mountain-array

"""
Simple Binary Search.
"""


class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        if len(A) < 3:
            return -1

        l, r = 0, len(A) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if A[mid - 1] < A[mid] > A[mid + 1]:
                return mid

            if A[mid] < A[mid + 1]:
                l = mid + 1
            else:
                r = mid - 1
        return -1
