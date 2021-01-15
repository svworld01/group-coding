/*
code by : Vivek pandey

*/
class Solution {
public:
    string removeDuplicates(string S) {
        stack <char> st;
        int i=0;
        int n = S.size();
        while(i<n){
            if(st.empty()){
                st.push(S[i]);
            }
            
           else if(st.top()==S[i]){
                st.pop();
            }
            else{
                st.push(S[i]);
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
