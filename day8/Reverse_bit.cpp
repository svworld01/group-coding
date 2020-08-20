
/*
code by : vivek pandey

problem link : https://leetcode.com/problems/reverse-bits

approach : bit approach 

*/

class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        
        uint32_t res =0, pow =31;
        while(n){
            res += (n & 1) << pow;
            //finding least significant bit and forcing it to its right position
            n = n >> 1;
            pow -= 1;
        }
        return res;
    }
};
