# created by KUMAR SHANU

# 1. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

## Solution 1
"""
The actual task is not to remove duplicates. the key point to focus on is the array is sorted.
you have to return the lenght of the array which contains the unique numbers at starting.

If array is:
[1, 1, 2]

you have to change the array as:
[1, 2, 2]
and return only the lenght of the unique part [1, 2] i.e. lenght = 2.
"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for n in nums:
            if n != nums[i]:
                i += 1
                nums[i] = n

        return i + 1


## Solution 2
"""
Two pointer solution.
"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        pointer1 = 0
        for pointer2 in range(len(nums)):
            if nums[pointer2] != nums[pointer1]:
                pointer1 += 1
                nums[pointer1] = nums[pointer2]

        return pointer1 + 1
