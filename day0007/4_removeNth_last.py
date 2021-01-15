# created by KUMAR SHANU

# 4. Remove Nth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = slow = head
        prev = None

        while n:
            n -= 1
            fast = fast.next

        while fast:
            fast = fast.next
            prev = slow
            slow = slow.next

        if prev is None:
            return head.next
        prev.next = slow.next
        return head
