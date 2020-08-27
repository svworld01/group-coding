/*
Code by : Vivek pandey 

problem link : https://leetcode.com/problems/make-the-string-great/submissions/

*/

class Solution {
public:
    string makeGood(string s) {
        stack <char> st;
        int i=0;
        int n = s.size();
        while(i<n){
            if(st.empty()){
                st.push(s[i]);
            }
            
           else if(islower(st.top()) && isupper(s[i])){
                if(toupper(st.top())==s[i]){
                    st.pop();
                }
               else{
                   st.push(s[i]);
               }
            }
            
           else if(isupper(st.top()) && islower(s[i])){
                  if(tolower(st.top())==s[i]){
                    st.pop();
                }
               else{
                   st.push(s[i]);
               }
            }
            else{
                st.push(s[i]);
            }
            i++;
        }
        string ans;
        while(!st.empty()){
            char a = st.top();
            st.pop();
            ans.push_back(a);
        }
        reverse(ans.begin(),ans.end());
        return ans;
    }
};                                  
