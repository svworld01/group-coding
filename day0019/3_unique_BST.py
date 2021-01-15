# created by KUMAR SHANU

# 3. Unique Binary Search Trees
# https://leetcode.com/problems/unique-binary-search-trees
import math


class Solution:
    def numTrees(self, n: int) -> int:
        # total no of BST from n nodes
        # C(2n, n)/ (n+1)
        return math.comb(2 * n, n) // (n + 1)
