# created by KUMAR SHANU

# 4. Kth Smallest Element in a BST
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

## Solution 1
"""
Using inorder traversal
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        inorder.traversal = []
        inorder(root)
        print(inorder.traversal)
        return inorder.traversal[k - 1]


def inorder(root):
    if root is None:
        return None

    inorder(root.left)
    inorder.traversal.append(root.val)
    inorder(root.right)


## Solution 2
"""
Using Stack
"""


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []

        while True:
            while root is not None:
                stack.append(root)
                root = root.left

            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right
