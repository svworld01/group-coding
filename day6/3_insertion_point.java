/*
Auther - Saurabh Verma
Problem link - https://leetcode.com/problems/find-smallest-letter-greater-than-target/
Time Complexity - O(logn)
*/
class Solution {
    public int searchInsert(int[] nums, int target) {
        int index = Arrays.binarySearch(nums, target);
        if(index >-1)
            return index;
        else
            return -index - 1;
    }
}
