/*
  
  *********Auther - Anand Keshari*************
  Problem Link - https://leetcode.com/problems/reverse-vowels-of-a-string/
  
  Time compleity - O(n)..................................................

                                                                                  */

class Solution {
public:
    string reverseVowels(string s) {
        unordered_set<char> vowel{'a','e','o','i','u','A','E','I','O','U'};
        int i=0,j=s.size()-1;
        while(i<j)
        {
            while(vowel.find(s[i])==vowel.end() && i<s.size()) i++;
            while(vowel.find(s[j])==vowel.end() && j>0) j--;
            if(i<j)
            {
                swap(s[i],s[j]);
                i++;
                j--;
            }
        }
        return s;
    }
    
};
