# created by KUMAR SHANU


# 3. Hamming Distance
# https://leetcode.com/problems/hamming-distance/
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        d = x ^ y
        c = 0
        while d:
            c += d & 1
            d >>= 1
        return c
