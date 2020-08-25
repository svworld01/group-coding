/*
Auther - Saurabh Verma
Problem link - https://leetcode.com/problems/remove-duplicates-from-sorted-array/
approach - use two pointer method to check duplicate
*/

class Solution {
    public int removeDuplicates(int[] nums) {
        if(nums.length <2)
            return nums.length;
        int prev = 0;
        int length = 1;
        int i = 1;
        for(int next = 1; next<nums.length; next++){
            if(nums[prev] == nums[next])
                continue;
            length++;
            nums[i++] = nums[next];
            prev = next;
        }
        return length;
    }
}
