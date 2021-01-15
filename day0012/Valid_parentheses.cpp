/*
code by : Vivek pandey

*/

class Solution {
public:
    bool isValid(string s) {
     stack<char> stk;
        int i=0;
        while(i<s.size())
        {
            if(stk.empty()){
                stk.push(s[i]);
            }
            else if(s[i]=='(' || s[i]=='{' || s[i]=='['){
                stk.push(s[i]);
            }
            else if(stk.top()=='(' && s[i]==')'){
                stk.pop();
            }
            else  if(stk.top()=='[' && s[i]==']'){
                stk.pop();
            }
            else if(stk.top()=='{' && s[i]=='}'){
                stk.pop();
            }
            else{
                return false;
            }
            i++;
        }
        if(stk.empty())
            return true;
        return false;
    }
};
