/*
*************************Auther- ANAND KESHARI****************************
problem Link- https://leetcode.com/problems/find-the-difference/

Time Complexity - O(n)
Space Complexity - O(n)
*/

class Solution {
public:
    char findTheDifference(string s, string t) {
        unordered_map<char,int> m;
        for(int i=0;i<s.size();i++)
        {
            if(m.find(s[i])==m.end())
            {
                m.insert(make_pair(s[i],1));
            }
            else
            {
                m[s[i]]++;
            }
        }
        char result;
        for(int i=0;i<t.size();i++)
        {
            if(m.find(t[i])==m.end() || m[t[i]]==0){
                result=t[i];
                break;
            }
            else
            {
                m[t[i]]--;
            }
        }
       return result;    
    }
};
