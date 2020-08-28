# created by KUMAR SHANU

# 2. Reverse Bits
# https://leetcode.com/problems/reverse-bits/


class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        pow = 31
        while n:
            res += (n & 1) << pow
            n = n >> 1
            pow -= 1
        return res
