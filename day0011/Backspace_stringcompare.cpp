/*
**********auther- anand keshari*******************

Problem link - https://leetcode.com/problems/backspace-string-compare/

*/

class Solution {
public:
    bool backspaceCompare(string S, string T) {
        stack<char> S1,T1;
        for(int i=0;i<S.length();i++)
        {
            if(S[i]!='#')
            {
                S1.push(S[i]);
            }
            else if(!S1.empty())
            {
                S1.pop();
            }
        }
        
        for(int i=0;i<T.length();i++)
        {
            if(T[i]!='#')
            {
                T1.push(T[i]);
            }
            else if(!T1.empty())
            {
                T1.pop();
            }
        }
        bool flag=true;
        if(S1.size()==T1.size())
        {
            while(S1.size())
            {
                if(S1.top()==T1.top())
                {
                    S1.pop();
                    T1.pop();
                }
                else
                {
                    flag=false;
                    break;
                }
            }
        }
        else
        {
            
            return false;
        }
        return flag;
    }
};
