/**
          &&&&&&&&&  Auther-Akash &&&&&&&&&&&&&&
          **********Approch****************
          create a temp  head.
          Then compare the first elements from each list. Add the smaller one to the merged list. 
          Finally, when one of them is empty, simply append it to the merged list, since it is already sorted.
          
          ***********

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
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
          if(l1 == null)
            return l2;
          if(l2 == null)
            return l1;
          ListNode head = new ListNode(0);
          //create a temp head    
          ListNode p=head;
 
          ListNode p1=l1;
          ListNode p2=l2;
          while(p1!=null && p2!=null){
          //checking first list min value and insert it in new list
          if(p1.val < p2.val){
            p.next = p1;
            p1 = p1.next;
        }else{//or check second list's min value and insert in the new list
            p.next = p2;
            p2 = p2.next;
        }
        //and increment the new list ponter or new insertion
        p=p.next;
    }
    //and in last when one of the is empty the add this in the new list 
    if(p1!=null){
        p.next = p1;
    }
 
    if(p2!=null){
        p.next = p2;
    }
    
    //finally return new list address    
    return head.next;
    }
}
