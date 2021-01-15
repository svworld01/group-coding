/*
***************Auther-  ANAND KESHARI****************
problem link-https://leetcode.com/problems/power-of-four/
Approach -
            4^1 =4=100;
            4^2 =16=10000;
            only most siggnificant value is set
            and no. of zeroes is even
 Time complexity- O(1) // as loop runs for maximum 64 times .
*/


class Solution {
public:
    bool isPowerOfFour(int num) {
        int count=0;
        if(num<1)
            return false;
        if(num && !(num & (num-1))) // check if the number has only one set value
        {
            while(num>1)
            {
                num=num>>1;
                count++;
            }
            if(count & 1)  //count is odd or even
            {
                return false;
            }
            else
                return true;
        }
        return false;
        
    }
};
