package day1;
/*
Solved by - Saurabh Verma
Problem link - https://leetcode.com/problems/running-sum-of-1d-array/
 */
class Solution1{

    public int[] runningSum(int[] nums) {
        for(int i=1; i<nums.length; i++){
            nums[i] += nums[i-1];
        }
        return nums;
    }
}