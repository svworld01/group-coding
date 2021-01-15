/*
Auther - Saurabh Verma
Problem link - https://leetcode.com/problems/remove-element/
Approach-
 consider the elements to be removed as non-existent. 
 In a single pass, if we keep copying the visible elements(not equal to given value ) in-place, that will solve this problem for us.
*/
class Solution {
    public int removeElement(int[] nums, int val) {
        int pointer = 0;
        for(int i=0; i<nums.length; i++){
            if(nums[i] != val){
                nums[pointer] = nums[i];
                pointer++;
            }
        }
        return pointer;
    }
}
