/*
Solution By - Saurabh Verma
*/
class Solution {
    public int matrixScore(int[][] A) {
        if(A.length == 0) return 0;
        
        for(int i = 0; i < A.length; i++) {
            if(A[i][0] == 0) {
                for(int j = 0; j < A[i].length; j++) {
                    A[i][j] = A[i][j] == 0 ? 1 : 0;
                }
            }
        }
		int count0;   
        for(int i = 1; i < A[0].length; i++) {
            count0 = 0;
            for(int j = 0; j < A.length; j++) {
                if(A[j][i] == 0) count0++;
            }
            if(count0 > A.length/2) {
                for(int k = 0; k < A.length; k++) {
                    A[k][i] = A[k][i] == 0 ? 1 : 0;
                }
            }
        }
        int binary;
        int total = 0;
        for(int i = 0; i < A.length; i++) {
            binary = 1;
            for(int j = A[i].length-1; j >=0 ; j--) {
                total += A[i][j] * binary;
                binary *= 2;
            }
        }
        
        return total;
    }
}
