/*
  Auther - Saurabh Verma
  problem link - https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
  Explanation - 
  1. use binaary search to find strength(number of 1's) of each row
  2. used priority queue (heap) to find K weakest to strongest row (you can also do it by sorting logic)
  
  time complexity - O(nlogn)
  space complexity - O(k)
*/
class Solution {
    public int[] kWeakestRows(int[][] mat, int k) {
        
        PriorityQueue<int[]> pq = new PriorityQueue<>(new MyComparator());
        int[] res = new int[k];
        
        for(int i=0; i<mat.length; i++){
            int index = binarySearch(mat[i]);
            pq.offer(new int[]{index , i});
            if(pq.size() > k){
                pq.poll();
            }
        }
        while(k > 0)
            res[--k] = pq.poll()[1];
        return res;
        
    }
    int binarySearch(int[] arr){
        int left = 0;
        int right = arr.length;
        while(left< right){
            int mid = (left + right-1) / 2;
            if(arr[mid] == 1){
                left = mid + 1;
            }else{
                right = mid;
            }
        }
        return left;
    }
}
// custom comparator
class MyComparator implements Comparator<int[]>{
    public int compare(int[] a, int[] b) {
       return a[0] != b[0] ? b[0] - a[0] : b[1] - a[1];
    }
}
