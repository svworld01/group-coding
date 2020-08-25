/*
Auther - Saurabh Verma
Problem link - https://leetcode.com/problems/number-of-good-pairs/
*/
package day2;
import java.util.HashMap;

class Solution {
    public int numIdenticalPairs(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<>();
        int pairs = 0;
        for(int n : nums){
            if(map.containsKey(n)){
                pairs += map.get(n);
                map.put(n, map.get(n)+1);
            }else{
                map.put(n, 1);
            }
        }
        return pairs;
    }
}