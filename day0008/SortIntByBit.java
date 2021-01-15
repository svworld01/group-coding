*****************Auther >> Akash (The Robust Coder)*******************
/*

Approch  :
Use Recursively Bubble Sort for sorting and Count bits Using Integer.bitCount Inbuilt function  :)




*/


class Solution {
    public int[] sortByBits(int[] arr) {
        return bubbleSort(arr, arr.length);
        
    }
    public int[] bubbleSort(int[] arr, int len){
        int i , temp;
        for(i = 0; i < len-1; i++){
            int bc1 = Integer.bitCount(arr[i]);
            int bc2 = Integer.bitCount(arr[i+1]);
            
            //Comparing Elements
            if((bc1 > bc2) || ((bc1 == bc2) && (arr[i] > arr[i+1]))) {
                temp = arr[i];
                arr[i] = arr[i+1];
                arr[i+1] = temp; 
            }
        }
        if(len == 0) return arr;
        //sort again whenevr we got arr lent 0
        return bubbleSort(arr, len-1);
    }
}
