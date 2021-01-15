/*
Auther - Saurabh Verma
Problem link - https://leetcode.com/problems/find-smallest-letter-greater-than-target/
Approach - binary Search
Time Complexity - O(logn)
*/
class Solution {
    public char nextGreatestLetter(char[] letters, char target) {
        int left = 0;
        int right= letters.length;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (letters[mid] <= target){ 
                left = mid + 1;
            }
            else {
                right = mid;
            }
        }
        return letters[left % letters.length];
    }
}
