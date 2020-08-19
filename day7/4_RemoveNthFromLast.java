/*
Solution By - Saurabh Verma
Problem link - https://leetcode.com/problems/remove-nth-node-from-end-of-list/
Time Complexity - O(n)
Space Complexity - O(1)
Approach - take two pointer fast and slow and traverse the loop maintaining the condition that fast - slow = n.
maintain prev as slow -1
remove slow using prev.
*/
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode fast = head;
        ListNode slow = head;
        ListNode prev = null;
        while(n-->0){
            fast = fast.next;
        }
        while(fast!=null){
            fast = fast.next;
            prev = slow;
            slow = slow.next;
        }
        if(prev == null)
            return head.next;
        prev.next = slow.next;
        return head;
        
    }
}
