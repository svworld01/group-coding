package day1;
import java.util.Arrays;
class Solution5 {
    public int findDuplicate(int[] nums) {
        Arrays.sort(nums);
        int result = nums[0];
        for(int i=0; i<nums.length; i++){
            if(i>0){
                int findLeft = Arrays.binarySearch(nums, 0, i, nums[i]);
                if(findLeft >= 0){
                    return nums[i];
                }
            }
            if(i+1 < nums.length){
                int findRight =  Arrays.binarySearch(nums, i+1, nums.length-1, nums[i]);
                if(findRight >= 0){
                    return nums[i];
                }
            }
        }
        return result;
    }
}