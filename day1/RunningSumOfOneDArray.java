package day1;

import java.util.Arrays;
/*
Solved by - Saurabh Verma
Problem link - https://leetcode.com/problems/running-sum-of-1d-array/
 */
public class RunningSumOfOneDArray{
    
    public int[] runningSum(int[] nums) {
        for(int i=1; i<nums.length; i++){
            nums[i] += nums[i-1];
        }
        return nums;
    }

    //main method for testing--
    public static void main(String[] args) {
        RunningSumOfOneDArray sol = new RunningSumOfOneDArray();
        int[] a = {1,2,3,4,5,6,7,8,9,10};
        int[] result = sol.runningSum(a);
        System.out.println(Arrays.toString(result));
    }
}