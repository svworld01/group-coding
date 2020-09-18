/*
Solution By - Saurabh Verma
*/
class Solution {
    public int numWaterBottles(int numBottles, int numExchange) {
        int drinks = 0;
        int empty = 0;
        while(numBottles > 0){
            drinks += numBottles;
            empty += numBottles;
            numBottles = empty / numExchange;
            empty %= numExchange;
        }
        return drinks;
    }
}
