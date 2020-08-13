package day1;
/*
Solved by - Saurabh Verma
Problem link - https://leetcode.com/problems/shuffle-the-array/
 */
class Solution3 {
    public int[] shuffle(int[] nums, int n) {
        int[] result = new int[2*n];
        int j = 0;
        //inserting half array
        for(int i=0; i<2*n; i=i+2){
            result[i] = nums[j];
            j++;
        }
        //inserting next half array
        for(int i=1; i<2*n; i=i+2){
            result[i] = nums[j];
            j++;
        }
        return result;
    }
}