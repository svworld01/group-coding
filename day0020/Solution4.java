/*
Solution By - Saurabh Verma
Problem Link - https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/
*/
class Solution {
    public int sum(int[] a){
        int sum = 0;
        for(int i:a)
            sum+= i;
        return sum;
    }
    public int largestSumAfterKNegations(int[] A, int K) {
        if(K==0)
            return sum(A);
        Arrays.sort(A);
        int i=0;
        while(i<A.length && A[i] <0 && K>0){
            if(A[i] < 0) A[i]*=-1;
            i++;
            K--;
        }
        Arrays.sort(A);
        if((K&1) == 1) A[0] *=-1;
        return sum(A);
    }
}
