/*
Auther - Saurabh Verma
Problem link - https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
Approach - Here, I'm using two pointer logic which have time complexity O(n), however you can also do it by
using binary search but it can take O(nlogn) in worst case
*/
class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int i=0; 
        int j = numbers.length - 1;
        while(i<j){
            int tmp = numbers[i] + numbers[j];
            if(tmp == target){
                return new int[]{i+1, j+1};
            }else if(tmp > target){
                j--;
            }else{
                i++;
            }
        }
        return new int[2];
    }
}
