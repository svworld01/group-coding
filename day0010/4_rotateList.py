# created by KUMAR SHANU

# 4. Rotate List
# https://leetcode.com/problems/rotate-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # base cases
        if k == 0 or head is None or head.next is None:
            return head
        # lenght
        l = 2
        prevlast = head
        while prevlast.next.next:
            prevlast = prevlast.next
            l += 1

        # rotate last element
        prevlast.next.next = head
        head = prevlast.next
        prevlast.next = None

        # rotate again (k-1) times
        return self.rotateRight(head, (k - 1) % l)
