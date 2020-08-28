# created by KUMAR SHANU

# 5. Subsets
# https://leetcode.com/problems/subsets/


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        size = 2**len(nums)
        for counter in range(size):
            curr = []
            for j in range(len(nums)):
                if (counter & (1 << j)) > 0:
                    curr.append(nums[j])
            res.append(curr)

        return list(res)
