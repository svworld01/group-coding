/*
Solution By - Saurabh Verma
*/

class Solution {
    public int minCost(String s, int[] cost) {
        if(s.length() <2)
            return 0;
        
        int ans = 0;
        int i = 0;
        int j = 1;
        
        while(j<s.length()){
            if(s.charAt(i) == s.charAt(j)){
                if(cost[i] > cost[j]){
                    ans += cost[j];
                    j++;
                }else{
                    ans += cost[i];
                    i=j;
                    j++;
                }
            }else{
                i=j;
                j++;
            }
        }
        return ans;
    }
}
