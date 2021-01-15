/*
Solution By - Saurabh Verma
Problem link - https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
*/

class Solution {
    public void flatten(TreeNode root) {
        solve(root);
    }
    public TreeNode solve(TreeNode root){
        if(root == null)
            return null;
        TreeNode left = solve(root.left);
        TreeNode right = solve(root.right);
        root.left = null;
        if(left!= null){
            root.right = left;
            while(left.right!=null)
                left = left.right;
            left.right = right;
        }
        return root;
    }
}
