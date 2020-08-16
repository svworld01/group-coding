/*
Auther- Saurabh Verma
Problem link - https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
Time Complexity- O(nlogn)
*/
class Solution {
    public int countNegatives(int[][] grid) {
        int count = 0;
        if(grid.length == 0) return 0;
        for(int i=0; i<grid.length; i++){
            int index  = binarySearch(grid[i], -1);
            
            if(index> -1)
                count += grid[i].length - index;
            else
                count += grid[i].length - (-1 * index -1);
        }
        return count;
    }
    int binarySearch(int a[], int srchVal){
        int lb = 0;
        int ub = a.length-1;
        int mid= 0;
        int index = a.length;
        while( lb <= ub){
            mid = (lb + ub +1)/2;
            if(a[mid] == srchVal){
               if(index > mid){
                    index = mid;
                    ub = mid -1;
                }
            }
            else if(srchVal > a[mid]){
               ub = mid - 1;
            }
            else{
                lb = mid + 1;
            }
         }
        if(index != a.length) return index;
        return -(lb +1);
    }
}
