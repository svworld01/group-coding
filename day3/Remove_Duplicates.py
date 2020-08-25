# created by Anand

# 1. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1

        while (i < len(nums)):
            if (nums[i] == nums[i - 1]):
                nums.pop(i)

            else:
                i = i + 1

        return len(nums)
