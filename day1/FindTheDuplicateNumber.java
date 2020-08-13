/*
Auther - Saurabh Verma
Problem link - https://leetcode.com/problems/find-the-duplicate-number/

there are three methods that I have found
-------------------------------------------------------------------------

#Method1- 
O(n) Time Complexity
using A[x] = -A[x] to check duplicate
*/
class Solution {
    public int findDuplicate(int[] nums) {
         for(int n:nums){
            int index = Math.abs(n) - 1;
           if(nums[index]<0){
               return Math.abs(n);
           }
            nums[index]*=-1;
        }
         return 0;
    }
}
/*
#Method 2   
O(n) time complexity
using BitSet in Java
*/
class Solution {
   public int findDuplicate(int[] nums) {
        BitSet bs = new BitSet(nums.length);
        for (int num : nums) {
            if (bs.get(num)) {
                return num;
            } else {
                bs.set(num, true);
            }
        }
        
        return -1;
    }
}
/*
#Method 3   
O(nlogn) time complexity
using BinarySearch method
*/
class Solution {
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
