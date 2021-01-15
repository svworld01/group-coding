/*
code by :Vivek pandey

*/


//next greater element
class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
    vector<int> ans;

    //taking a map for storing the next greter element for every number
    unordered_map <int,int> m;
    if(nums2.empty()) return ans;
    int n = nums2.size();
    m[nums2[n-1]] = -1;  //we know that the last element will no greater element
    stack<int> s;
    s.push(nums2[n-1]);

    for(int i=n-2;i>=0;i--){    //finding next greater elememt

        while(!s.empty() && s.top()<nums2[i]){
            s.pop();
        }
        if(!s.empty()){
            m[nums2[i]] = s.top();
        }
        else{
            m[nums2[i]] = -1;
        }
        s.push(nums2[i]);
    }
    int nn=nums1.size();

    for(int i=0;i<nn;i++){
        ans.push_back(m[nums1[i]]);
    }
    return ans;
    }
};
