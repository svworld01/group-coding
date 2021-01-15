# created by KUMAR SHANU

# 5. Kth Smallest Element in a Sorted Matrix
# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

# Solution 1
"""
Solution using Binary Search.
Time complexity : O(nlog(MaxVal))

"""


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # store min and max values
        low = matrix[0][0]
        high = matrix[len(matrix) - 1][len(matrix) - 1]
        ans = low

        # apply binary search on min and max value
        while low <= high:

            mid = (low + high) // 2

            # count the number of elements <= mid
            num = self.count(matrix, mid)

            if num < k:
                low = mid + 1
            elif num >= k:
                # store the result
                ans = mid
                high = mid - 1

        return ans

    def count(self, matrix, mid):
        i = len(matrix) - 1
        j = 0

        # counter
        c = 0
        while i >= 0 and j < len(matrix):
            if matrix[i][j] > mid:
                i -= 1
            else:
                c += i + 1
                j += 1

        return c


# Solution 2
"""
Solution using Heap.

"""
import heapq


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # initialize empty heap
        heap = []
        for row in matrix:
            # push each element of matrix into heap
            for num in row:
                heapq.heappush(heap, num)

        for i in range(k - 1):
            # pop k-1 times to get kth smallest element
            heapq.heappop(heap)

        return heap[0]
