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
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
 
 /*
      ******************Auther--Akash*******************
      problem :: https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree
 
 
 */
class Solution {
    public TreeNode sortedListToBST(ListNode head) {
        ListNode p = new ListNode(-1);
        p.next = head;
        int count = 0;
        ListNode node = head;
        while (node!=null) {
            count ++;
            node = node.next;
        }
        return genrateBinaryTree(p, 0, count - 1);
    }
    private TreeNode genrateBinaryTree(ListNode p, int start, int end){
        if (start > end) {
            return null;
        }
        int mid = (start + end) / 2;
        TreeNode left = genrateBinaryTree(p, start, mid - 1);
        TreeNode root = new TreeNode(p.next.val);
        p.next = p.next.next;
        TreeNode right = genrateBinaryTree(p, mid + 1, end);
        root.left = left;
        root.right = right;
        return root;
    }
}
