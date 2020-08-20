/**

    Solved by : Vivek pandey
    
    problem link : https://leetcode.com/problems/merge-k-sorted-lists/
    
    approach : divide and conquer 
    
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
    
    ListNode* add(ListNode* a,ListNode* b){
       //chceking for empty
        if(a==NULL)
            return b;
        if(b==NULL)
            return a;
        //creating new list
        ListNode* ans = NULL;
        //adding value by comparing
        if(a->val <= b->val){
            ans = a;
            ans->next = add(a->next ,b);
        }
        else{
            ans = b;
            ans->next = add(a,b->next);
        }
        //and returing
        return ans;
    }
    
    
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        // 
        int n =lists.size();
        if(n==0){
            return NULL;
        }
        if(n==1){
            return lists[0];
        }
        if(n==2){
            return add(lists[0],lists[1]);
        }
        //dividing the problem in smaller ones
        vector< ListNode* > l1(lists.begin() , lists.begin()+n/2);
        vector<ListNode* > l2(lists.begin()+n/2,lists.end());
        //then solving the problem in merging fashion
        return add(mergeKLists(l1),mergeKLists(l2));
    }
};
