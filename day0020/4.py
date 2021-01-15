# created by KUMAR SHANU

# 4. Maximize Sum Of Array After K Negations
# https://leetcode.com/problems/maximize-sum-of-array-after-k-negations


class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        # base case
        if K == 0:
            return sum(A)
        else:
            # sort the array
            A.sort()
            i = 0
            while i < len(A) and K > 0 and A[i] < 0:
                if A[i] < 0:
                    A[i] = A[i] * -1
                i += 1
                K -= 1
            A.sort()
            if (K & 1) == 1:
                A[0] = A[0] * -1
            # returning the sum
            return sum(A)
