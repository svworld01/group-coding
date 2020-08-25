/* code by : vivek pandey

problem link : https://leetcode.com/problems/linked-list-cycle/

approach : 
        using two pointer method; */



/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
     ListNode* slow = head;
        ListNode* fast = head;
        while(fast!=NULL){
            slow = slow->next;
            if(slow==NULL){
                return false;
            }
            if(fast->next==NULL){
                return false;
            }
            fast = fast->next->next;
            if(slow==fast){
                return true;
            }
        }
        return false;
    }
};
