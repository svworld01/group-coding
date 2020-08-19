# created by KUMAR SHANU

# 4. Find the Smallest Divisor Given a Threshold
# https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l, r = 1, nums[-1]

        while l < r:
            mid = l + (r - l) // 2
            res = sum([ceil(x / mid) for x in nums])
            if res > threshold:
                l = mid + 1
            elif res <= threshold:
                r = mid
        return l
