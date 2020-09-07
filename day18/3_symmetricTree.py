# created by KUMAR SHANU

# 3. Symmetric Tree
# https://leetcode.com/problems/symmetric-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive Solution
"""
A tree is symmetric if it's left subtree and right subtree are mirror of each other.
If we can check two tree are mirror or not we can found our answer.
"""


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirror(root, root)

    def isMirror(self, t1, t2):
        # Empty Tree
        if t1 is None and t2 is None:
            return True
        # if one tree is Empty
        if t1 is None or t2 is None:
            return False
        # Mirror condition
        return (t1.val == t2.val) and self.isMirror(
            t1.right, t2.left) and self.isMirror(t1.left, t2.right)


# Iterative Solution
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        queue = []
        queue.append(root)
        queue.append(root)
        while queue != []:
            t1 = queue.pop(0)
            t2 = queue.pop(0)
            if t1 is None and t2 is None:
                continue
            if t1 is None or t2 is None:
                return False
            if t1.val != t2.val:
                return False
            queue.append(t1.left)
            queue.append(t2.right)
            queue.append(t1.right)
            queue.append(t2.left)
        return True
