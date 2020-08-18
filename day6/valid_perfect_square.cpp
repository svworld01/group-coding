/*
code by : vivek pandey

problem link : https://leetcode.com/problems/valid-perfect-square


*/

  
bool chek( long long int  l,int n){
    if(l*l == n){
        return true;
    }
    else if(l*l<n){
        return chek(l+1,n);
    }
    else 
        return false;
}

class Solution {
public:
    bool isPerfectSquare(int num) {
        long long int i=1;
        bool ans = chek(i,num);
        return ans;
    }
};
