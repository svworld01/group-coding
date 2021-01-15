/*
code by : vivek pandey

Problem link : https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position 

*/


Solution 

class Solution {
public:
    int minCostToMoveChips(vector<int>& position) {
        int odd =0;
        int even=0;
        unordered_map <int,int> m;
        for(int i=0;i<position.size();i++){
            m[position[i]]++;
        }
        for(auto i=m.begin();i!=m.end();i++){
            if(i->first%2==0)
                even += i->second;
            else
                odd += i->second;
        }
        return odd<even?odd:even;
    }
};
