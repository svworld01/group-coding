# created by KUMAR SHANU

# 4. Counting Bits
# https://leetcode.com/problems/counting-bits/


class Solution:
    def countBits(self, num: int) -> List[int]:
        ans = [0] * (num + 1)
        for i in range(1, num + 1):
            ans[i] = ans[i // 2] + i % 2
        return ans
