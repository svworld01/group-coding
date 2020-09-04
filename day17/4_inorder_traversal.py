# created by KUMAR SHANU

# 4. Binary Tree Inorder Traversal
# https://leetcode.com/problems/binary-tree-inorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution 1
"""
Using recursion.
"""


class Solution:
    def __init__(self):
        self.lst = []

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.inorder(root)
        return self.lst

    def inorder(self, root):
        if not root:
            return None
        self.inorder(root.left)
        self.lst.append(root.val)
        self.inorder(root.right)


# Solution 2
"""
Without using recursion.
"""


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # initialize stack
        stack = []
        # initialize list for store inorder traversal
        lst = []

        # if tree is empty
        if root is None:
            return lst

        # pointer to the root of the tree
        ptr = root

        while True:
            # if node exists
            if ptr:
                # push it to stack
                stack.append(ptr)
                ptr = ptr.left

            # if node doesnot exists and stack is not empty
            elif stack != []:
                # pop node from stack
                ptr = stack.pop(-1)
                # traverse it
                lst.append(ptr.val)
                ptr = ptr.right

            # if node doesnot exixts and stack is empty
            # we are done here return the result
            else:
                return lst
