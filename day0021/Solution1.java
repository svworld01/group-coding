/*
Solution By  - Saurabh Verma
Problem link - https://leetcode.com/problems/delete-columns-to-make-sorted/
*/
class Solution {
    public int minDeletionSize(String[] A) {
        int count = 0;
        int length = A[0].length();
        for (int i = 0; i < length; i++) {
            for (int j = 0; j < A.length-1; j++) {
                if(A[j].charAt(i) > (A[j+1].charAt(i))){
                    count++;
                    break;
                }
            }
        }
        return count;
    }
}
