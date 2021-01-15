  /* 
code by :  Vivek pandey 

problem link :  https://leetcode.com/problems/counting-bits/

approach : //Brain kernigham algo

*/

class Solution {
public:
    
    //Brain kernigham algo
    int count(int n){
        int cc=0;
        while(n){
            n &= (n-1);
            cc++;
        }
        return cc;
    }
    
    vector<int> countBits(int num) {
        vector <int> v;
        for(int i=0; i<=num;i++){
            int cnt = count(i);
            v.push_back(cnt);
        }
        return v;
    }
};
