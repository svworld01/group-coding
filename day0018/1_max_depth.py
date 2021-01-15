# created by KUMAR SHANU

# 1. Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # if tree empty
        if not root:
            return 0

        # find depth of left subtree
        l = self.maxDepth(root.left)

        # find depth of right subtree
        r = self.maxDepth(root.right)

        # find max of left and right subtree add 1 for root
        return (l + 1) if l > r else (r + 1)
