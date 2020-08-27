/*
code by :Vivek pandey

Problem Link : https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/submissions/

*/


class Solution {
public:
    int minAddToMakeValid(string S) {
        stack<char> st;
        int i=0;
        int n =S.size();
        while(i<n){
            if(st.empty()){
                st.push(S[i]);
            }
            else if(st.top()=='(' && S[i]==')'){
                    st.pop();  
            }
            else{
                st.push(S[i]);
            }
            i++;
        }
        return st.size();
    }
};
