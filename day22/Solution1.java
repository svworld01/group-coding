/*
Solution By - Saurabh Verma
*/
class Solution {
    public int minCostToMoveChips(int[] position) {
        int even = 0;
        int odd = 0;
        for(int i: position){
            if((i&1) == 1)
                odd++;
            else
                even++;
        }
        return Math.min(even, odd);
    }
}
