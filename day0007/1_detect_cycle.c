// created by KUMAR SHANU

// Solution using two pointers
// one is fast pointer
// one is slow pointer

// 1. Linked List Cycle
// https://leetcode.com/problems/linked-list-cycle/


/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool hasCycle(struct ListNode *head) {
    struct ListNode *slow=head, *fast=head;
    
    while(slow && fast && fast->next){
        slow = slow->next;
        fast = fast->next->next;
        if(slow==fast)
            return true;
    }
    return false;
}
