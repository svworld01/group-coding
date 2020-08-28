# created by KUMAR SHANU

# 3. Convert Sorted List to Binary Search Tree
# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        ptr = head
        lst = []
        while ptr:
            lst.append(ptr.val)
            ptr = ptr.next
        return self.BST(lst, 0, len(lst) - 1)

    def BST(self, lst, low, high):
        if low > high:
            return None

        mid = low + (high - low) // 2
        root = TreeNode(lst[mid])
        if low == high:
            return root
        root.left = self.BST(lst, low, mid - 1)
        root.right = self.BST(lst, mid + 1, high)
        return root
