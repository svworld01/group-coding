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
    public ListNode rotateRight(ListNode head, int k) {
        // Check for base case
        if (k == 0) return head;
        // Check if rotation is actually required
        if (head == null || head.next == null) return head;
        
        // Find the node before the last node,
    
        ListNode beforeLast = head;
        //after checking those conditions above we have minimum lenth of list is 2
        int length = 2;
        while (beforeLast.next.next != null) {
            beforeLast = beforeLast.next;
            length += 1;
        }

        // Do one rotation
        beforeLast.next.next = head;
        head = beforeLast.next;
        beforeLast.next = null;

        // rotate again for next k
        return rotateRight(head, (k - 1) % length);
    }
}

           
