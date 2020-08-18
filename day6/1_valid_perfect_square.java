/*
Auther - Saurabh Verma
Problem link - https://leetcode.com/problems/valid-perfect-square/
Aproach - using binary search to perfect find sqare root
Time Complexity - O(logn)
Space Complexity - O(1)
*/
class Solution {
    public boolean isPerfectSquare(int num) {
        long left = 1;
        long right = (num+1)/2;
        while(left<=right){
            long mid = (left + right) / 2;
            long square = mid*mid;
            if( square == num)
                return true;
            else if(square < num){
                left = mid + 1;
            }else{
                right = mid - 1;
            }
        }
        return false;
    }
}
