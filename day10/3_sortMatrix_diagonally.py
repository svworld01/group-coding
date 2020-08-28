# created by KUMAR SHANU

# 3. Sort the Matrix Diagonally
# https://leetcode.com/problems/sort-the-matrix-diagonally/

# Solution 1
"""
store each diagonal into the dictionary and sort.
"""
from collections import defaultdict


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        d = defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                # store diagonal into dictionary
                diff = i - j
                d[diff].append(mat[i][j])

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                # sort the diagonal
                diff = i - j
                d[diff].sort()
                # insert it back to matrix
                mat[i][j] = d[diff].pop(0)

        return mat


# Solution 2
"""
Using dict and heap
"""
import heapq


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        d = defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                # push diagonal into heap
                diff = i - j
                heapq.heappush(d[diff], mat[i][j])
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                diff = i - j
                mat[i][j] = heapq.heappop(d[diff])

        return mat
