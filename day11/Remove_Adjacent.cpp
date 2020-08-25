/*
**********auther- Anand Keshari****************

problem link- https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
*/
class Solution {
public:
    string removeDuplicates(string S) {
        stack<char> unique;
        for(int i=0;i<S.size();i++)
        {
            if(unique.empty() || S[i]!=unique.top())
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
