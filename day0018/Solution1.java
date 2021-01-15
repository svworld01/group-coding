/*
Solution By  - Saurabh Verma
Problem link - https://leetcode.com/problems/maximum-depth-of-binary-tree/
*/
class Solution {
    public int maxDepth(TreeNode root) {
        if (root == null)
            return 0;
        int left = 1 + maxDepth(root.left);
        int right = 1 + maxDepth(root.right);
        return Math.max(left, right);
    }
}
