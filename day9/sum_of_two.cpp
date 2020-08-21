(9) Sum of Two Integers - LeetCode/*
code by : vivek pandey

*/

class Solution {
public:
    int getSum(int a, int b) {
        int carry =0;
        while(b){
            int carry = a & b;  //finding arry form here
            a = a ^b;   //implementation like half addar
            b =(unsigned int) carry<<1; //for handing the negative values;
        }
        return a;
    }
};
