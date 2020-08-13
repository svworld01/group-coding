/*
Solved by - Saurabh Verma
Problem link - https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
 */

package day1;
import java.util.*;

class Solution2 {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        
        List<Boolean> result = new ArrayList<>();
        int max = Integer.MIN_VALUE;
        //getting max value
        for(int num : candies)
            if( num > max)
                max = num;
        //finding all greater than and equal to max value and make them true 
        for(int i=0; i<candies.length; i++){
            if(candies[i]+extraCandies >= max)
                result.add(true);
            else
                result.add(false);
        }
        return result;
        
    }
}