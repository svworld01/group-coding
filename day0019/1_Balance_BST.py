# created by KUMAR SHANU

# 1. Balance a Binary Search Tree
# https://leetcode.com/problems/balance-a-binary-search-tree
"""
1. Convert BST to arr using inorder traversal
2. Construct a New Balanced BST
3. return root of new constructed tree
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        # inorder traversal
        inorder = self.inorderTraversal(root)
        # construct new BST
        return self.constructBST(inorder, 0, len(inorder) - 1)

    def constructBST(self, arr, start, end):
        root = None
        if start <= end:
            mid = start + (end - start) // 2
            root = TreeNode(arr[mid])
            ptr = root
            ptr.left = self.constructBST(arr, start, mid - 1)
            ptr.right = self.constructBST(arr, mid + 1, end)
        return root

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
