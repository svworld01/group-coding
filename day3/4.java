/*
Auther - Saurabh Verma
Problem link - https://leetcode.com/problems/3sum-closest/
*/
class Solution {
    public int threeSumClosest(int[] nums, int target) {
        int n = nums.length;
        int low=0;
        int high=0;
        int min=Integer.MAX_VALUE;
        int ans=0;
        Arrays.sort(nums);
        for(int i=0;i<n-2;i++){
            low = i+1;
            high = n-1;
            while(low<high){
                int sum = nums[i]+nums[low]+nums[high];
                int diff = Math.abs(target - sum);
                if(diff < min){
                    min = diff;
                    ans = sum;
                }
                if(sum == target) return sum;
                else if(sum > target) high--;
                else low++;
            }
        }
        return ans;
    }
}
