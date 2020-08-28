// created by KUMAR SHANU

// 4. Sum of Two Integers
// https://leetcode.com/problems/sum-of-two-integers/

int getSum(int a, int b){
    int max, min, carry;

    max = (a > b) ? a : b;
    min = (a > b) ? b : a;
    while (max != 0)
    {
        carry = min & max;
        min = min ^ max;

        // convert into unsigned int to deal with negative numbers
        max = (unsigned int)carry << 1;
    }
    return min;
}
