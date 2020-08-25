/*
Auther - Saurabh Verma
Problem link - https://leetcode.com/problems/koko-eating-bananas/
Explanation - https://www.youtube.com/watch?v=t3Tq_iyzl8E
*/
class Solution {
    public  int minEatingSpeed(int[] piles, int H) {
        int high = Integer.MIN_VALUE; 
        for(int i=0; i<piles.length; i++){
            high = high < piles[i]? piles[i]: high;
        }
        int low  = 1;
        int ans = high;
        while(low <= high){
            int mid = (low + high) / 2;
            if(findTimeWithSpeed(piles, mid) <= H){
                if(ans > mid)
                    ans = mid;
                high = mid -1 ;
            }else{
                low = mid + 1;
            } 
        }
        return ans;

    }
    public int findTimeWithSpeed(int[] piles, int speed){
        int h = 0;
        for(int p: piles)
            h += (p+speed -1) / speed;
        return h;
    }
}
