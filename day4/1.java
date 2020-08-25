/*
Auther - Saurabh Verma
Problem link - https://leetcode.com/problems/binary-search/
*/
class Solution {
    public int search(int[] nums, int target) {
        int index = Arrays.binarySearch(nums, target);
        return index>-1?index:-1;
    }
}
