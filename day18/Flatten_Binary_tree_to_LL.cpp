/*
code by : Vivek pandey


problem link : https://leetcode.com/problems/flatten-binary-tree-to-linked-list

*/

Solutiuon 


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
    void reverse(TreeNode* root){
        if(root==nullptr)
            return ;
        reverse(root->left);
        reverse(root->right);
        
        TreeNode* tem = root->left;
        root->left =  root->right;
        root->right = tem;
        
    }
    
    void flatten(TreeNode* root) {
        reverse(root);
        stack<TreeNode* > S;
        while(root!=nullptr || !S.empty()){
            if(root->left!=nullptr ){
                S.push(root->left);
                root->left = nullptr;
            }
            if(root->right==nullptr && !S.empty()){
                root->right = S.top();
                S.pop();
                
            }
            root= root->right;
        }
    }
};
