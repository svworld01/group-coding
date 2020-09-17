/*
Solution By - Saurabh Verma
Problem link - https://leetcode.com/problems/queue-reconstruction-by-height/
*/
class Solution {

     public int[][] reconstructQueue(int[][] people) {
     
        //create a result list
        List<int[]> res = new ArrayList<>(people.length);
        
        //sort array by h in descending and then k in ascending
        Arrays.sort(people, (a, b) -> {
            return (a[0] == b[0]) ? a[1] - b[1] : b[0] - a[0];
        });
        //put every person at its k index in arraylist as it will shift already existing element, we shall get right answer
        for (int[] p : people)
            res.add(p[1], p);
            
        //reset people by result 
        for (int i = 0; i < res.size(); i++)
            people[i] = res.get(i);
        
        //return result
        return people;
    }
}
