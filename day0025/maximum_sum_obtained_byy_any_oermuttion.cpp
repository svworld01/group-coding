/*
code by :Vivek pandey

problem  link : 


Approach : Discrete inpulus signal sort.


*/
Solution :
 
 class Solution {
public:
    int maxSumRangeQuery(vector<int>& nums, vector<vector<int>>& requests) {
        int n= nums.size();
        vector<int> v(n+1,0);
        for(auto i: requests){
            v[i[0]] +=1;
            v[i[1]+1] -=1;
        }
        
        v.pop_back();
        
        for(int i=1;i<n;++i){
            v[i] += v[i-1];
        }
        
        sort(v.begin(),v.end());
        sort(nums.begin(),nums.end());
        int m = 1e9 +7;
        int ans =0;
        for(int i=0;i<n;++i){
            ans = (ans + nums[i]*v[i])%m;
        }
        return ans;
    }
};
