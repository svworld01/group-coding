/*
Solution By - Saurabh Verma
Explanation - https://leetcode.com/problems/split-array-into-consecutive-subsequences/discuss/844738/Java-or-Very-easy-explanation-through-a-story-or-Time-O(n)-Space-O(n)
*/
class Solution {
    public boolean isPossible(int[] nums) {
        HashMap<Integer,Integer> avaibilityMap = new HashMap<>();
        HashMap<Integer,Integer> wantMap = new HashMap<>();
        for(int i : nums){
            avaibilityMap.put(i, avaibilityMap.getOrDefault(i,0)+1);
        }
        for(int i=0;i<nums.length;i++){
            if(avaibilityMap.get(nums[i])<=0){
                continue;
            }
            else if(wantMap.getOrDefault(nums[i],0)>0){
                avaibilityMap.put(nums[i], avaibilityMap.getOrDefault(nums[i],0)-1);
                wantMap.put(nums[i], wantMap.getOrDefault(nums[i],0)-1);
                wantMap.put(nums[i]+1, wantMap.getOrDefault(nums[i]+1,0)+1);
            }
            else if(avaibilityMap.getOrDefault(nums[i],0)>0 && avaibilityMap.getOrDefault(nums[i]+1,0)>0 && avaibilityMap.getOrDefault(nums[i]+2,0)>0){
                avaibilityMap.put(nums[i], avaibilityMap.getOrDefault(nums[i],0)-1);
                avaibilityMap.put(nums[i]+1, avaibilityMap.getOrDefault(nums[i]+1,0)-1);
                avaibilityMap.put(nums[i]+2, avaibilityMap.getOrDefault(nums[i]+2,0)-1);
                wantMap.put(nums[i]+3, wantMap.getOrDefault(nums[i]+3,0)+1);
            }
            else{
                return false;
            }
        }
        return true;
    }
}
