**************solution 1 with Built in function**********

/*class Solution {
    public int[] countBits(int num) {
        int len=num+1;
        int res[]=new int[len];
        for(int i=0;i<=num;i++){
            res[i]=countBitiInI(i);
        }
        return res;
    }
    public int countBitiInI(int num){
        return Integer.bitCount(num);
    }
}*/
********************solution 2 By Using Custom Logic after binary pattern of numbers*********
    class Solution {
    public int[] countBits(int num) {
        int[] arr = new int[num + 1];
        for (int i = 0; i <= num; i++) {
            if (i % 2 == 0) {
              arr[i] = arr[i / 2];
            }
            else {
              arr[i] = 1 + arr[i-1];
              }
        }
        return arr;
    }
}

