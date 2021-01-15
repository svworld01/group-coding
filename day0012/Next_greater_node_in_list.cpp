/*
code by : Vivek pandey

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
    vector<int> nextLargerNodes(ListNode* head) {
        vector<int> v;
        ListNode* temp1 =head;
        while(temp1!=NULL){
            ListNode* temp2 = temp1;
            int n = v.size();
            int dt = temp1->val;
            while(temp2!=NULL){
                if(temp2->val > dt){
                    v.push_back(temp2->val);
                    break;
                }
                temp2= temp2->next;
            }
            if(n==v.size()){
                v.push_back(0);
            }
            temp1 = temp1->next;
        }
        return v;
    }
};
