/*
Solved by - Saurabh Verma
Problem link - https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

Approach->
create a result list
find max value
loop 0 to n
    check if current value is greater than equal to max
        add true into result list
    else
        add false into result list
 */

class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        
        List<Boolean> result = new ArrayList<>();
        int max = Integer.MIN_VALUE;
        //getting max value
        for(int num : candies)
            if( num > max)
                max = num;
        //finding all greater than and equal to max value and make them true into result
        for(int i=0; i<candies.length; i++){
            if(candies[i]+extraCandies >= max)
                result.add(true);
            else
                result.add(false);
        }
        return result;
        
    }
}
