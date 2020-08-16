# created by KUMAR SHANU

# 3. Shuffle the Array
# https://leetcode.com/problems/shuffle-the-array/


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr = []
        i = 0
        j = n
        while (i < n) and (j < 2 * n):
            arr.append(nums[i])
            arr.append(nums[j])
            i += 1
            j += 1
        return arr
