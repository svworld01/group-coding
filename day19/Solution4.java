/*
Solution By  - Saurabh Verma
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
class Solution {
    public List<TreeNode> generateTrees(int n) {
        if(n <= 0) 
            return new LinkedList<>();
        return generate(1, n);
    }
    private List<TreeNode> generate(int left, int right) {
        List<TreeNode> result = new LinkedList<>();
        if (left > right) {
            result.add(null);
            return result;
        }
        for (int i = left; i <= right; i++) {
            // generate subtrees on left making root = i
            List<TreeNode> leftTrees = generate(left, i - 1);        
            // generate subtrees on right making root = i             
            List<TreeNode> rightTrees = generate(i + 1, right);
            for (TreeNode leftTree : leftTrees) {
                for (TreeNode rightTree : rightTrees) {
                    TreeNode root = new TreeNode(i);
                    root.left = leftTree;
                    root.right = rightTree;
                    result.add(root);
                }
            }
        }
        return result;
    }
}
