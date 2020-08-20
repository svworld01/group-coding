/**



    solved by:  vivek pandey
    
    problem link : https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
    
    approach : divide and concqure 
    
    
    
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
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
    ListNode* find(ListNode* start,ListNode* end){
        ListNode* p= start;
        ListNode* q= start;
        //finding the middle element by two pointer
        while(q->next!=end && q->next->next!=end){
            p = p->next;
            q = q->next->next;
        }
        return p;
    }
    
    TreeNode* bst(ListNode* start, ListNode* end){
        //base condition
        if(start==end || start==NULL){
            return NULL;
        }
        //finding the middle element
        ListNode* mid = find(start,end);
        TreeNode* tree =new TreeNode;
        //adding middle element in root
        tree->val = mid->val;
        //adding first half in left of Binary search tree
        tree->left = bst(start,mid);
        //adding second half in the right of BST
        tree->right = bst(mid->next,end);
        return tree;
    }
    
    TreeNode* sortedListToBST(ListNode* head) {
    //checking if head is empty
        if(head==NULL)
            return NULL;
        TreeNode *root;
        //caliig function to make
        root = bst(head,NULL);
        return root;
    }
};
