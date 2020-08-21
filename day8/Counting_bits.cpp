/*
  ****************Auther- Anand Keshari*********************
  Problem link - https://leetcode.com/problems/counting-bits/
*/

class Solution {
public:
    vector<int> countBits(int num) {
        vector<int> bits{0};
        int j=1;
        for(int i=1;i<=num;i++)
        {
            if(i==j*2)
            {
                j=j*2;
            }
            bits.push_back(1+bits[i-j]);
        }
        return bits;
    
    }
    
};
