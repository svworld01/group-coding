# created by KUMAR SHANU

# 1. Binary Search
# https://leetcode.com/problems/binary-search/


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find boundaries
        l, r = 0, len(nums) - 1

        while l <= r:

            # find middle element
            mid = l + (r - l) // 2

            # base case
            # return index if middle element is equal to target
            if nums[mid] == target:
                return mid

            # if middle element is smaller than target
            # reduce the search to left subarray
            if nums[mid] < target:
                l = mid + 1

            # if middle element is smaller than target
            # reduce the search to left subarray
            else:
                r = mid - 1

        return -1
