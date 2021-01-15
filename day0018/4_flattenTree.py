# created by KUMAR SHANU

# 4. Flatten Binary Tree to Linked List
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return

        # intialize stack
        stack = []
        stack.append(root)
        while stack != []:

            # get current node
            curr = stack.pop(-1)

            # push right child into stack
            if curr.right:
                stack.append(curr.right)

            # push left child into stack
            if curr.left:
                stack.append(curr.left)

            if stack != []:
                curr.right = stack[-1]
            curr.left = None
