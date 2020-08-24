# created by KUMAR SHANU

# 5. Merge k Sorted Lists
# https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Solution 1
"""
Merge two lists at a time.
"""


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        head = lists[0]
        for i in range(1, len(lists)):
            head = self.mergeTwolists(head, lists[i])

        return head

    def mergeTwolists(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        head = ListNode()
        ptr = head

        while l1 and l2:
            if l1.val < l2.val:
                ptr.next = l1
                l1 = l1.next
            else:
                ptr.next = l2
                l2 = l2.next
            ptr = ptr.next
        if l1:
            ptr.next = l1
        if l2:
            ptr.next = l2
        return head.next


# Solution 2
"""
Solution using heap.
"""
import heapq


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        for head in lists:
            while head:
                heapq.heappush(heap, head.val)
                head = head.next
        dummy = ListNode()
        head = dummy
        while heap:
            head.next = ListNode(heapq.heappop(heap))
            head = head.next

        return dummy.next
