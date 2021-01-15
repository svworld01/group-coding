# created by KUMAR SHANU

# 5. 4 Sum
# https://leetcode.com/problems/4sum/


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        arr = []
        for i in range(len(nums) - 3):
            if i != 0 and (nums[i] == nums[i - 1]):
                continue
            for j in range(i + 1, len(nums) - 2):
                if j != i + 1 and (nums[j] == nums[j - 1]):
                    continue
                l, r = j + 1, len(nums) - 1
                while (l < r):
                    s = nums[i] + nums[j] + nums[l] + nums[r]
                    if s > target:
                        r -= 1
                    elif s < target:
                        l += 1
                    else:
                        arr.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while (l < r) and (nums[l] == nums[l - 1]):
                            l += 1
                        while (l < r) and (nums[r] == nums[r + 1]):
                            r -= 1
        return arr
