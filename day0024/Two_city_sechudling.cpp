/* code by :Vivek pandey

Problem link : https://leetcode.com/problems/two-city-scheduling/

solution */


class Solution {
public:
     
    int twoCitySchedCost(vector<vector<int>>& costs) {
        vector<pair<int,pair<int,int>>> v;
        for(auto i: costs){
            v.push_back({i[0]-i[1],{i[0],i[1]}});
        }
        sort(begin(v),end(v));
        int cnt=0,n=costs.size()/2;
        for(auto j:v){
            if(n-- >0)
                cnt += j.second.first;
            else
                cnt += j.second.second;
        }
        return cnt;
    }
};
