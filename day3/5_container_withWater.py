# created by KUMAR SHANU

# 5. Container With Most Water
# https://leetcode.com/problems/container-with-most-water/


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)

        # if container is not exists
        if n == 0 or n == 1:
            return 0

        # initialize two pointers one from left and one from right
        i, j = 0, n - 1

        # keep track of maximum area
        area = 0
        while i < n and i <= j:

            # claculate distance between the vertical lines
            d = j - i

            curr_area = 0
            if height[i] < height[j]:
                curr_area = height[i] * d
                i += 1
            else:
                curr_area = height[j] * d
                j -= 1

            # update area
            if curr_area > area:
                area = curr_area

        return area
