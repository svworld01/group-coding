/*
Auther - Saurabh Verma
Problem link - https://leetcode.com/problems/intersection-of-two-arrays/
*/
class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        Set<Integer> set1 = new HashSet<>();
        Set<Integer> set2 = new HashSet<>();
        
        for(int i:nums1) set1.add(i);
        for(int i:nums2) set2.add(i);
        
        set1.retainAll(set2);
        
        int[] res = new int[set1.size()];
        int i =0;
           for(int n: set1)
               res[i++] = n;
        return res;
    }
}
