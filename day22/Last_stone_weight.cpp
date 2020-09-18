/*Code by :Vivek pandey

Problem link : https://leetcode.com/problems/last-stone-weight

*/

Solution 

class Solution {
public:
    int last(vector<int> &v,int i){
        sort(v.begin(),v.end());
        while(i>=0){
            if(i==0){
                return v[i];
            }
            else{
                if(v[i]==v[i-1]){
                    v.pop_back();
                    v.pop_back();
                    return last(v,i-2);
                }
                else{
                    v[i-1]= v[i]-v[i-1];
                    v.pop_back();
                    return last(v,i-1);
                }
            }
        }
        return 0;
    }
    int lastStoneWeight(vector<int>& stones) {
        if(stones.size()==1){
            return stones[0];
        }
        return last(stones,stones.size()-1);
    }
};
