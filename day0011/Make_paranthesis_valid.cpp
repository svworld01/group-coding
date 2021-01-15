/*
****************auther- Anand Keshari***************
problem Link - https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
*/

class Solution {
public:
    int minAddToMakeValid(string S) {
        stack<char> Invalid;
        for(int i=0;i<S.length();i++)
        {
            if(Invalid.empty() || S[i]==Invalid.top() || S[i]=='(' && Invalid.top()==')')
            {
                Invalid.push(S[i]);
            }
            else
            {
                Invalid.pop();
            }
        }
        return Invalid.size();
    }
};
