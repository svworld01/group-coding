/* code by : Vivek Pandey

Problem link :https://leetcode.com/problems/water-bottles


*/

Solution

class Solution {
public:
    int numWaterBottles(int Bottle, int  ex ) {
        int rem=0,max=Bottle;
        int cnt = Bottle;
        while(max>=ex){
            cnt += max/ex;
            rem = max%ex;
            max = max/ex;
            max += rem;
        }
        return cnt;
    }
};
