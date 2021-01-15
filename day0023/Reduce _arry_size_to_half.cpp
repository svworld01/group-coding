/*
code by :Vivek pandey

Prolem link : https://leetcode.com/problems/reduce-array-size-to-the-half


Solution 

*/

class Solution {
public:
    int minSetSize(vector<int>& arr) {
        int n= arr.size();
        map<int,int> m;
        for(int i=0;i<n;i++){
            m[arr[i]]++;
        }
        int cnt=0,sum=0;
        set<pair<int,int>> s;
        for(auto i=m.begin();i!=m.end();i++){
            s.insert(make_pair(i->second,i->first));
        }
        for(auto j=s.rbegin();j!=s.rend();j++){
            sum += (j->first);
            cnt++;
            if(sum >=n/2){
                return cnt;
            }
        }
        return cnt;
    }
};
