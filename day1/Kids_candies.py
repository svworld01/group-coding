# created by KUMAR SHANU

# 2. Kids With the Greatest Number of Candies
# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)
        return [((candy + extraCandies) >= max_candy) for candy in candies]
        
        
