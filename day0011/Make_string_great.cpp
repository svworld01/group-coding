/*
************auther - Anand Keshari******************
problem_link- https://leetcode.com/problems/make-the-string-great/
                                                                    */
                                                                    
                                                                    
class Solution {
public:
    string makeGood(string S) {
        stack<char> unique;
        for(int i=0;i<S.size();i++)
        {
            if(unique.empty() )
            {
                unique.push(S[i]);
            }
            else if(S[i]==unique.top())
            {
                unique.push(S[i]);
            }
            else if((S[i] & '_') != unique.top() && (S[i] | ' ')!=unique.top())
            {
                unique.push(S[i]);
            }
            else
            {
                unique.pop();
            }
        }
        string res;
        while(!unique.empty())
        {
            res+=unique.top();
            unique.pop();
        }
        reverse(res.begin(),res.end());
        return res;
    }
};
