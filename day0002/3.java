/*
Auther - Saurabh Verma
Problem link -  https://leetcode.com/problems/xor-operation-in-an-array/
*/

package day2;
class Solution {
    public int xorOperation(int n, int start) {
        int xor = start;
        for(int i=1; i<n; i++){
            xor ^= start + 2*i;
        }
        return xor;
    }
}