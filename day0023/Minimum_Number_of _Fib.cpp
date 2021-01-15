 /*
 code by : Vivek pandey 
 
 Problem link : https://leetcode.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/
 
 solution */
 
 class Solution {
public:
    int findLarge(int k){
        int i=1,j=1;
            while(j<k){
                int te= j;
                j = i + j;
                i= te;
            }
        return (j==k)?k:i;
    }
    int fibFind(int k){
        if(k<0){
            return 0;
        }
        int largestFib = findLarge(k);
        if(largestFib ==k){
            return 1;
        }
        return 1+ fibFind(k-largestFib);
    }
    
    int findMinFibonacciNumbers(int k) {
        return fibFind(k);
    }
};
