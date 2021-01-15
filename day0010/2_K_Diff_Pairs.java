/*
Auther - Saurabh Verma
Problem link - https://leetcode.com/problems/k-diff-pairs-in-an-array/
Approach - use hashmap to store frequency of each value to handle k ==0 case
*/
class Solution {
    public int findPairs(int[] nums, int k) {
        HashMap<Integer, Integer> map = new HashMap<>();
        int count = 0;
        for(int i: nums)
            map.put(i, map.getOrDefault(i, 0)+1);
        for(Map.Entry<Integer, Integer> e: map.entrySet()){
            
            if(k == 0 && e.getValue() > 1)
                count++;
            else if(k>0 && map.containsKey(e.getKey() + k))
                count++;
        }
        return count;
    }
}
