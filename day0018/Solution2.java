/*
Solution By  - Saurabh Verma
*/
class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if(p==null && q == null)
            return true;
        if(p==null || q == null)
            return false;
        boolean result = p.val == q.val;
        return result && isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
    }
}
