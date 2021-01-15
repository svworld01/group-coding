/*
  ******************auther- Anand Keshari********************
  problem link - https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/
*/
int bit_count(int a)
    {
        unsigned int count=0;
        while(a)
        {
            if(a & 1)
                count++;
            a=a>>1;
        }
        return count;
    }
bool cmp(int a1, int a2 )
    {
        if(bit_count(a1)<bit_count(a2))
            return true;
        else if(bit_count(a1)>bit_count(a2))
            return false;
        return a1<a2;
    }
class Solution {
public:
    vector<int> sortByBits(vector<int>& arr) {
       sort(arr.begin(),arr.end(),cmp);
        return arr;
    }
    
    
};
