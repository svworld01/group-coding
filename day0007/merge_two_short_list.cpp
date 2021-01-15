
/**
code by:  vivek pandey

problem link : https://leetcode.com/problems/merge-two-sorted-lists/


approach : merging like merge sort






 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        //checking if list2 is empty
        if(!l1)return l2;
        //checking if list1 is empty
        if(!l2)return l1;
        
        //creating new node
        ListNode* newone = NULL;
        //ading a element in newnode
        if(l1->val <= l2->val){
            newone = l1;
            l1 = l1->next;
        }
        else{
            newone = l2;
            l2 = l2->next;
        }
        //creating new node 
        ListNode* temp = newone;
        //pauring all element with comparing
        while(l1!=NULL && l2!=NULL){
            if(l1->val<=l2->val){
                temp->next= l1;
                l1 = l1->next;
            }
            else{
              temp->next = l2;
                l2 = l2->next;
            }
            temp = temp->next;
        }
        //pouring the remaing element
        if(l1!=NULL){
            temp->next = l1;
            }
        
        if(l2!=NULL){
            temp->next= l2;
            }
        return newone;
    }
};
