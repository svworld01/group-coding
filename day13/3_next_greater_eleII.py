# created by KUMAR SHANU

# 3. Next Greater Element II
# https://leetcode.com/problems/next-greater-element-ii

# Solution
"""
Because array is circular.
We consider array [1,2,1] as [1,2,1,1,2,1]
"""


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # initialize stack
        stack = []

        # initialize resultant array
        # fill it with -1
        ans = [-1] * len(nums)

        for i in range(len(nums) * 2):
            while stack and (nums[stack[-1]] < nums[i % len(nums)]):
                ans[stack.pop(-1)] = nums[i % len(nums)]

            # push index into stack
            if i < len(nums):
                stack.append(i)
        return ans
