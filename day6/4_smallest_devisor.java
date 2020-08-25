/*
Auther - Saurabh Verma
Problem link - https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/
Approach - use binary search and take left = 1 and right = max value of array beacuase if you go beyond of it u will get same answer.
*/
class Solution {
    public int smallestDivisor(int[] A, int threshold) {
        int left = 1;
        int right = A[A.length-1];
        while (left < right) {
            int m = (left + right) / 2;
            int sum = 0;
            for (int i : A)
                sum += (i + m - 1) / m;
            if (sum > threshold)
                left = m + 1;
            else
                right = m;
        }
        return left;
    }
}
