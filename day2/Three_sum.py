# created by KUMAR SHANU

# 4. 3 Sum
# https://leetcode.com/problems/3sum/

## Solution 1
"""
BruteForce Approach
search all the combinations and check for if the sum is 0
"""

from itertools import combinations
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        for k in range(len(nums)-2):
            i,j = k+1, len(nums)-1
            if(k==0 or (k>0 and nums[k]!= nums[k-1])):
                while i<j:
                    x = nums[i]+ nums[j] + nums[k]
                    if x ==0:
                        res.add(tuple(sorted((nums[i], nums[j], nums[k]))))
                    if x>0:
                        j -=1
                    else:
                        i +=1
        return list(list(i) for i in res)
        

## Solution 2
"""
Using Two_sum's Approach.
Faster solution Using Dict(Hash).
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sorting the array
        nums.sort()
        
        # creating the dict
        d = dict()
        # set to stor unique items
        arr = set()
        
        for i  in range(len(nums)):
            # fix the element and treat it as sum and find two elements whose sum equal to it
            s = -nums[i]
            
            if(i==0 or i>0 and nums[i] != nums[i-1]):
                for j in range(i+1, len(nums)):
                    key = s - nums[j]
                    
                    if key in d and (d[key] !=i) and (d[key]!=j):
                        # Find the tuple of three values and add them to set after sorting to avoid duplicate sol..
                        arr.add(tuple(sorted((nums[i], nums[j], nums[d[key]]))))
                    else:
                        d[nums[j]] = j
                        
        # return result as List[List] after converting to the list  
        return list(list(i) for i in arr)
        
