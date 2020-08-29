/*
        auther - Anand Keshari
        problem_link- https://leetcode.com/problems/valid-parentheses/
        
*/

class Solution {
public:
    bool isValid(string s) {
        stack<char> brackets;
        for(int i=0;i<s.size();i++)
        {
            if(s[i]=='(' || s[i]=='[' || s[i]=='{')
                brackets.push(s[i]);
            else if(brackets.empty())
            {
                return false;
            }
            else
            {
                if(brackets.top() < s[i] && s[i] < brackets.top()+3)
                {
                    brackets.pop();
                }
                else
                    return false;
            }
        }
        return brackets.empty();
    }
};
