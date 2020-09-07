# created by KUMAR SHANU

# 2. Same Tree
# https://leetcode.com/problems/same-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Solution 1
class Solution:
    def __init__(self):
        self.isSame = True

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        self.check(p, q)
        return self.isSame

    def check(self, p, q):
        if not p and not q:
            return False
        if not p and q:
            self.isSame = False
            return

        if p and not q:
            self.isSame = False
            return

        if p.val != q.val:
            self.isSame = False
        self.check(p.left, q.left)
        self.check(p.right, q.right)


# Solution 2
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None or q is None:
            return p == q
        if p.val != q.val:
            return False
        l = self.isSameTree(p.left, q.left)
        r = self.isSameTree(p.right, q.right)
        return l and r
