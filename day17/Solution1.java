/*
Solution By - Saurabh Verma
Problem Link - https://leetcode.com/problems/contains-duplicate
*/

class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for(int i: nums){
            if(!set.add(i))
                return true;
        }
        return false;
    }
}
