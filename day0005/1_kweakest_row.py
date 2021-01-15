# created by KUMAR SHANU

# 1. The K Weakest Rows in a Matrix
# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # dictionary(hash) to store
        d = dict()

        for i in range(len(mat)):
            # store number of the soldiers into dictionary
            d[i] = sum(mat[i])

        # sort the dict by values
        d = {key: value for (key, value) in sorted(d.items(), key=lambda kv: kv[1])}
        return list(d.keys())[:k]
