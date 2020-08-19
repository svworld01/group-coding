/*
Auther - Saurabh Verma
Problem Link - https://leetcode.com/problems/merge-k-sorted-lists/
Approach - use mergeTwoSortedList() logic
TimeComplexity - O(kN)
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
    public ListNode mergeKLists(ListNode[] lists) {
        if(lists.length == 0)
            return null;
        if(lists.length == 1)
            return lists[0];
        ListNode head = lists[0];
        for(int i=1; i<lists.length; i++){
            head = mergeTwoLists(head, lists[i]);
        }
        return head;
    }
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if(l1 == null)
            return l2;
        if(l2 == null)
            return l1;
        ListNode merged = null;
        ListNode tmp = null;
        if(l1.val < l2.val){
            merged = l1;
            l1 = l1.next;
        }else{
            merged = l2;
            l2 = l2.next;
        }
        tmp = merged;
        while(l1!= null && l2!= null){
            if(l1.val < l2.val){
                tmp.next = l1;
                l1 = l1.next;
            }else{
                tmp.next = l2;
                l2 = l2.next;
            }
            tmp = tmp.next;
        }
        if(l1!=null)
            tmp.next = l1;
        if(l2!=null)
            tmp.next = l2;
        return merged;
    }
}
