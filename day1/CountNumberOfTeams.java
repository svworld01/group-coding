/*
Auther -> Saurabh Verma  
Problem link -> https://leetcode.com/problems/count-number-of-teams/

Approach->
teams = 0
loop i=0 to n
    
    //treat each ith index as middle element of the team (x, y, z)
    lesser = find lesser value count to the left side of i
    greater = find greater value count to the right side of i
    cuont += lesser in left * greater in right
    count += greater in left * lesser in right
end loop
return teams
*/
package day1;
class Solution {

    public int numTeams(int[] rating) {

        //team count variable
        int teams = 0;

        /*loop through all the index, and considering 
        each ith index as middle rating among three ratings*/
        for (int i = 0; i < rating.length; i++) {

            int lesser = 0;
            int greater = 0;

            //counting lesser value in left side of i
            for (int j = 0; j < i; j++) {
                if (rating[i] > rating[j]) {
                    ++lesser;
                }
            }

            //counting greater value in right side of i
            for (int j = i + 1; j < rating.length; j++) {
                if (rating[i] < rating[j]) {
                    ++greater;
                }
            }

            //increasing team count
            teams += lesser * greater;
            //decreasing team count
            teams += (i - lesser) * (rating.length - 1 - i - greater);
        }

        return teams;
    }
}
