/**                                                  ***************Auther--Akash*******************
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
       
        int len = 0;
        ListNode temp = head;
        while(temp != null){
            temp = temp.next;
            len ++;
        }
        int toDel = len - n;
        ListNode p1 = new ListNode(-1);
        ListNode parent = p1;
        parent.next = head;
        while (toDel > 0){
            parent = parent.next;
            toDel --;
        }//end while
        parent.next = parent.next.next;
        return p1.next;
   
    }end function
}//end class
