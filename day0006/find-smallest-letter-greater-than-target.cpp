/*

code by: vivek pandey

problem link : https://leetcode.com/problems/find-smallest-letter-greater-than-target

*/


    class Solution {
public:
    char nextGreatestLetter(vector<char>& letters, char target) {
        char ans ;
        int g = (int)target -97;
        int prev =10000000;
        for(int i=0;i<letters.size();i++){
            int t = letters[i]-97;
            t = t+25 -g;
            t= t%26;
            int a =(int)ans -97;
            if(prev>t && letters[i]-97!=g){
                ans = letters[i];
                prev = t;
            }
             
        }
        return ans;
    }
};
