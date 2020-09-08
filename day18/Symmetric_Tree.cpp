 /* code by : Vivek pandey
 
 problem Link : https://leetcode.com/problems/symmetric-tree
 
 */
 
 
 Solution
 
 /**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    void inorder(TreeNode* roo,vector<int> &v){
        if(roo==NULL){
            v.push_back(-111);
            return;
        }
        inorder(roo->left,v);
        v.push_back(roo->val);
        inorder(roo->right,v);
        
    }
    bool isMirror(TreeNode* p, TreeNode* q){
        if(p==nullptr && q==nullptr){
            return true;
        }
        if(p==nullptr || q==nullptr){
            return false;
        }
        if(p->val==q->val){
            return isMirror(p->left,q->right) && isMirror(p->right,q->left);
        }
        else{
            return false;
        }
    }
    
    bool isSymmetric(TreeNode* root) {
        if(root==NULL)
            return true;
        return isMirror(root->left,root->right);
    }
};
