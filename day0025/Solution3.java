/*
Solution By - Saurabh Verma
*/
class Solution {
    public int maxSumRangeQuery(int[] nums, int[][] requests) {
        int n  = nums.length;
        long res = 0;
        int[] count = new int[n];
        long mod = 1000000007;
        for(int[] req : requests){
            count[req[0]]++;
            if(req[1]+1< n)
                count[req[1]+1]--;
        }
        for(int i=1; i<n; i++){
            count[i] += count[i-1];
        }
        Arrays.sort(nums);
        Arrays.sort(count);
        for(int i=0; i<n; i++){
            res += (long)nums[i] * count[i];
        }
        return (int)(res%mod);
    }
}
