# created by KUMAR SHANU

# 4. 3Sum Closest
# https://leetcode.com/problems/3sum-closest/


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        result = nums[0] + nums[1] + nums[-1]

        # sorting the array
        nums.sort()
        for i in range(len(nums) - 2):
            # initializing two pointers
            pointer1, pointer2 = i + 1, len(nums) - 1

            while (pointer1 < pointer2):

                # calculate the surrent sum
                curr_sum = nums[i] + nums[pointer1] + nums[pointer2]

                # if sum is greater than move the second pointer
                # otherwise first pointer
                if curr_sum > target:
                    pointer2 -= 1
                else:
                    pointer1 += 1

                if abs(curr_sum - target) < abs(result - target):
                    result = curr_sum

        return result
