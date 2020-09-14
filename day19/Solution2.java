/*
Solution By - Saurabh Verma
Problem link - https://leetcode.com/problems/search-in-rotated-sorted-array/
*/
class Solution {
    public int search(int[] nums, int target) {
        int s = 0;
        int e = nums.length-1;
        while(s <= e)
        {
            int mid=(s+e)/2;
            if(nums[mid]==target)
                return mid;
            else if(nums[mid]>nums[nums.length-1])
            {
                if(nums[mid]<target || target<nums[0])
                    s=mid+1;
                else
                    e=mid-1;
            }
            else 
            {
                if(target<nums[mid] || target>nums[nums.length-1])
                    e=mid-1;
                else
                    s=mid+1;
            }
        }
        return -1;
        
    }
}
