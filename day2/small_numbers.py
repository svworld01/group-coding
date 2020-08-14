# created by KUMAR SHANU

# 2. How Many Numbers Are Smaller Than the Current Number
# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

## Solution 1
"""
Simple solution
"""

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = [] 
        for i in range(len(nums)) :
            cnt =0
            for j in range(len(nums)) :
                if i!=j and (nums[j] < nums[i]):
                    cnt +=1
            arr.append(cnt)
        return arr
        
        
## Solution 2
"""
Faster solution using sort method.
"""

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        a = sorted(nums)
        for i in range(len(nums)):
            nums[i] = a.index(nums[i])
        return nums
        
