/*
      auther-Anand Keshari
      problem_link-  https://leetcode.com/problems/score-of-parentheses/
*/

class Solution {
public:
    int scoreOfParentheses(string s) {
        int n=s.size(),temp1,temp2;
        stack<int>stk;
        stk.push(0);
        for(int i=0;i<n;i++)
        {
            if(s[i]=='(')
                stk.push(0);
            else
            {
                temp1=stk.top();stk.pop();
                temp2=stk.top();stk.pop();
                if(temp1==0)
                {
                    
                    stk.push(temp1+1+temp2);
                }
                else
                {
                    stk.push(temp1*2+temp2);
                }
            }
        }
        return stk.top();
    }
};
