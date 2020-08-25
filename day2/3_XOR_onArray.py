# created by KUMAR SHANU

# 3. XOR Operation in an Array
# https://leetcode.com/problems/xor-operation-in-an-array/

## Solution 1
"""
Using reduce and lambda.
"""


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        arr = [start + 2 * i for i in range(n)]
        return reduce(lambda x, y: x ^ y, arr)


## Solution 2
"""
Simple and fast solution.
"""


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        res = 0
        for i in range(n):
            res ^= start + 2 * i
        return res
