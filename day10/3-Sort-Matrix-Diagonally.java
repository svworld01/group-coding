/*
Auther - Saurabh Verma
Problem link - https://leetcode.com/problems/sort-the-matrix-diagonally/
Time Complexity- (m*n)log(min(m,n))
*/

class Solution {
    public int[][] diagonalSort(int[][] mat) {
        Map<Integer, PriorityQueue<Integer>> map = new HashMap<>();
        for(int i=0; i<mat.length; i++){
            for(int j=0; j<mat[i].length; j++){
               int diff = i - j;
                if(map.containsKey(diff)){
                    map.get(diff).add(mat[i][j]);
                }else{
                    map.put(diff, new PriorityQueue());
                    map.get(diff).add(mat[i][j]);
                }
            }
        }
        for (int i = 0; i < mat.length; i++) {
            for (int j = 0; j < mat[i].length; j++) {
                mat[i][j] = map.get(i-j).poll();
            }
           
        }
        return mat;
        
    }
}
