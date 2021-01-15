/*
Solution By - Saurabh Verma
Problem link - https://leetcode.com/problems/balance-a-binary-search-tree/
*/
class Solution {
    public TreeNode balanceBST(TreeNode root) {
        if(root == null)
             return root;
        
        List<Integer> list = new ArrayList<Integer>();
        inOrderTraversal(root, list);
        return createbalancedBST(list, 0, list.size() -1);
    }
    void inOrderTraversal(TreeNode root, List<Integer> list){
        if(root == null)
            return;
        inOrderTraversal(root.left, list);
        list.add(root.val);
        inOrderTraversal(root.right, list);
    }
    TreeNode createbalancedBST(List<Integer> list, int start, int end){
        if(start >  end){
            return null;
        }
        int mid = (start + end) /2;
        TreeNode node = new TreeNode(list.get(mid));
        node.left = createbalancedBST(list, start, mid-1);
        node.right = createbalancedBST(list, mid+1, end);
        return node;
    }
}
