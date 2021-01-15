# created by KUMAR SHANU

# 2. Search in Rotated Sorted Array
# https://leetcode.com/problems/search-in-rotated-sorted-array/


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums is None or len(nums) == 0:
            return -1

        # Do binary search to find index of min element
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        # store min index into start
        # and do binary search to find target
        start = left
        left = 0
        right = len(nums) - 1

        # finding the right bounries to do binary search
        if target >= nums[start] and target <= nums[right]:
            left = start
        else:
            right = start

        # Simple binary search
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
