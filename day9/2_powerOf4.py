# creted by KUMAR SHANU

# 2. Power of Four
# https://leetcode.com/problems/power-of-four/


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if (num and (num & num - 1) == 0 and (num & 0xAAAAAAAAA) == 0):
            return True
        else:
            return False
