/*
Solved by - Saurabh Verma
Problem link - https://leetcode.com/problems/running-sum-of-1d-array/

Approach->
loop from index 1 to n
    add previous value to current index 
end loop
 */
class Solution1{

    public int[] runningSum(int[] nums) {
        for(int i=1; i<nums.length; i++){
            nums[i] += nums[i-1];
        }
        return nums;
    }
}
