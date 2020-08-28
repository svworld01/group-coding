# created by KUMAR SHANU

# 5. Integer Replacement
# https://leetcode.com/problems/integer-replacement/


class Solution:
    def integerReplacement(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 0

        count = 0
        while n > 1:
            if n % 2 == 0:
                n //= 2
            else:
                if n == 3 or (n // 2) % 2 == 0:
                    n -= 1
                else:
                    n += 1
            count += 1
        return count
