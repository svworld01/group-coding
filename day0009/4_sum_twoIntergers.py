# created by KUMAR SHANU

# 4. Sum of Two Integers
# https://leetcode.com/problems/sum-of-two-integers/


class Solution:
    def getSum(self, a: int, b: int) -> int:
        if a > b:
            max, min = a, b
        else:
            max, min = b, a

        mask = 0xffffffff
        while max & mask:
            carry = (min & max)
            min = min ^ max
            max = (carry << 1)
        return min & mask if max > mask else min


print(Solution().getSum(2, 3))
