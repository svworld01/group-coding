/**

    solved by : Vivek pandey
    
    problem link : https://leetcode.com/problems/remove-nth-node-from-end-of-list/
    
    approach : find the position from beginging and delete it normal

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
    int find(ListNode* head,int nn){
        int cn=0;
        while(head!=NULL){
            cn++;
            head = head->next;
        }
        return cn-nn-1;
    }
    
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        if(head==NULL)
            return NULL;
        
        int num = find(head,n);
        ListNode* temp = head;
        
        if(num==-1){
            head = temp->next;
            delete(temp);
        }
        else{
        while(num--){
            temp= temp->next;    
        }
        if(temp->next->next==NULL){
            temp->next  = NULL;
        }
        else{
            ListNode* ter =temp->next;
            temp ->next = ter->next;
            delete(ter);
        }
            }
        return head;
    }
};
