/*
 * Problem link - https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/
*/

//  Definition for a binary tree node.
   class TreeNode {
      int val;
      TreeNode left;
      TreeNode right;
      TreeNode() {}
      TreeNode(int val) { this.val = val; }
      TreeNode(int val, TreeNode left, TreeNode right) {
          this.val = val;
          this.left = left;
          this.right = right;
      }
  }

public class SplitBinaryTree {
    long sum = 0l;
    long max = 0l;
    public int maxProduct(TreeNode root) {
        sum = totalSum(root);
        findMax(root);
        return (int)((long)max%1000000007);
    }
    public long totalSum(TreeNode root){
        if(root == null) return 0;
        return root.val + totalSum(root.left) + totalSum(root.right);
    }
    public long findMax(TreeNode root){
        if(root == null) return 0;
        
        long f = findMax(root.left);
        long s = findMax(root.right);
        
        max = Math.max(Math.max((sum-f) * f, (sum-s) * s), max);
        return f+s+root.val;
    }
}