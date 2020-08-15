# created by KUMAR SHANU

# 2. Remove Element
# https://leetcode.com/problems/remove-element/


## Solution 1
"""
Two pointer solution.
"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        # if array contains only elements equals to val
        if nums == [val]*len(nums):
            return 0
        
        # intialize two pointers p1 left->right and p2 left<-right
        p2 = len(nums)-1
        
        #print(nums)
        for p1 in range(len(nums)):
            
            # move the pointer if the pointer points to the val which have to remove
            while nums[p2] == val:
                p2 -= 1
            
            # base case
            if p1 >= p2:
                #print(nums)
                return p2+1
            
            # swap the elements to the last of the array 
            if nums[p1] == val and nums[p2] != val:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p2 -= 1

## Solution 2
"""
consider the elements to be removed as not visible.
we keep copying the visible elements(not equal to given value) in-place.
"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pointer = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[pointer] = nums[i]
                pointer += 1
        return pointer              
                
