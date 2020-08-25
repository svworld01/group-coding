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
        
        //checking list is exist or not
        if(head==null){
            return false;
        }
     //find a cycle in list
        while(p1!=p2){
         //checking last node pointer
            if(p2==null||p2.next==null){
                return false;
            }
         //if thus is not last point to the next both pointer p1 and p2
            p1=p1.next;
            p2=p2.next.next;
        }
        return true;
    }
}
