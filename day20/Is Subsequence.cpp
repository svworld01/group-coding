/*
code by: Vivek pandey

Approach BY : Greedy

*/


class Solution {
public:
    bool isSubsequence(string s, string t) {
        int n= s.length();
        int cn=0;
        int i=0;
        int j=0;
        while(i<n && j<t.size()){
            if(s[i]==t[j]){
                i++;j++;
                cn++;
            }
            else{
                j++;
            }
        }
        if(cn==n)
            return true;
        return false;
    }
};
