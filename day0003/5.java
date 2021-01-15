/*
Auther - Saurabh Verma
Problem link - https://leetcode.com/problems/container-with-most-water/submissions/
*/
class Solution {
    public int maxArea(int[] height) {
        if(height.length == 0 || height.length == 1) 
            return 0;

        int max = Integer.MIN_VALUE;
        int high = height.length-1;
        int low = 0;
        while(high > low) {
            max = Math.max(max, Math.min(height[high], height[low]) * (high - low));
            if(height[high] > height[low]) {
                low++;
            }else {
                high--;
            }
        }
        return max;
    }
}
