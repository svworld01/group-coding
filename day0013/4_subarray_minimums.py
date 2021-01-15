# created by KUMAR SHANU

# 4. Sum of Subarray Minimums
# https://leetcode.com/problems/sum-of-subarray-minimums

# Solution from -
# https://www.geeksforgeeks.org/sum-of-minimum-elements-of-all-subarrays/


class Solution:
    def sumSubarrayMins(self, A) -> int:
        # intialize two array left and right
        l, r = [None] * len(A), [None] * len(A)

        # use two stacks
        s1, s2 = [], []

        # finding left subarray
        for i in range(len(A)):
            c = 1
            while s1 and (s1[-1][0] >= A[i]):
                c += s1[-1][1]
                s1.pop(-1)

            s1.append([A[i], c])
            l[i] = c

        # finding right subarray
        for i in range(len(A) - 1, -1, -1):
            c = 1
            while s2 and (s2[-1][0] > A[i]):
                c += s2[-1][1]
                s2.pop(-1)
            s2.append([A[i], c])
            r[i] = c

        # Now calculate the sum
        result = 0
        for i in range(len(A)):
            result += A[i] * l[i] * r[i]

        return result % (10**9 + 7)


print(Solution().sumSubarrayMins([3, 1, 2, 4]))
