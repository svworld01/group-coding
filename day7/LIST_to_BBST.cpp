
/**
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
 /************************* auther- Anand Keshari*************************** 
  Problem Link- https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
 */
class Solution {
public:
    TreeNode* sortedListToBST(ListNode* head) {
        int n=count(head);
        cout<<n;
        return BST(&head,0,n-1);
        
    }
    int count(ListNode* head)
    {
        ListNode* node= new ListNode;
        node=head;
        int temp=0;
        while(node!=NULL)
        {
            temp++;
            node=node->next;
        }
        return temp;
    }
    TreeNode* BST(ListNode** p, int lo, int hi)
    {
        if(lo>hi)
            return NULL;
        int mid=(lo+hi)/2;
        TreeNode* left= BST(p,lo,mid-1);
        TreeNode* root=new TreeNode;
        root->val=(*p)->val;
        *p=(*p)->next;
        TreeNode* right= BST(p,mid+1,hi);
        root->left=left;
        root->right=right;
        return root;
    }
    
};
