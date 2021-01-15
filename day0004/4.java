/*
Auther - Saurabh Verma
Problem link - https://leetcode.com/problems/kth-smallest-element-in-a-bst/
*/
class Solution {
    public int kthSmallest(TreeNode root, int k) {
         Stack<TreeNode> stack = new Stack<TreeNode>();

        while (true) {
          while (root != null) {
            stack.push(root);
            root = root.left;
          }
          root = stack.pop();
          if (--k == 0) return root.val;
          root = root.right;
        }
    }
}
