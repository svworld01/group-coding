/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 
 Auther ---Akash
 */


public class Solution {
    public boolean hasCycle(ListNode head) {
        
        ListNode p1=head;
        ListNode p2=p1.next;
        if(head==null){
            return false;
        }
        while(p1!=p2){
            if(p2==null||p2.next==null){
                return false;
            }
            p1=p1.next;
            p2=p2.next.next;
        }
        return true;
    }
}
