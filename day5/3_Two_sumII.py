# created by KUMAR SHANU

# 3. Two Sum II - Input array is sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # initialize two pointers
        i, j = 0, len(numbers) - 1

        while i < j:

            if (numbers[i] + numbers[j]) == target:
                return [i + 1, j + 1]

            elif (numbers[i] + numbers[j]) > target:
                j -= 1

            else:
                i += 1

        return [None] * 2
