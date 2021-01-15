# created by KUMAR SHANU

# 5. Next Greater Node In Linked List
# https://leetcode.com/problems/next-greater-node-in-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        node_vals = []
        ptr = head
        # convert list into array
        while ptr:
            node_vals.append(ptr.val)
            ptr = ptr.next

        # initialize stack
        stack = []

        # resultant array
        ans = [0] * len(node_vals)
        for i in range(len(node_vals)):
            while stack and (node_vals[stack[-1]] < node_vals[i]):
                ans[stack.pop(-1)] = node_vals[i]

            # push index into stack
            stack.append(i)

        return ans
