/*
*********auther- Anand keshari****************

problem link- https://leetcode.com/problems/rotate-list/

***********Time Complexity- O(n)************************
*/

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
class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if(head==NULL)
            return head;
        ListNode* ptr1= new ListNode;
        ListNode* ptr2= new ListNode;
        ptr1=head;
        ptr2=head;
        int cnt=1;
        while(ptr2->next!=NULL) 
        {
            cnt++;
            ptr2=ptr2->next;
        }
        k=k%cnt;
        k=cnt-k-1;
       // if(k==0)
         //   return head;
        while(k>0)
        {
            ptr1=ptr1->next;
            k--;
        }
        ptr2->next=head;
        head=ptr1->next;
        ptr1->next=NULL;
        return head;
    }
};
