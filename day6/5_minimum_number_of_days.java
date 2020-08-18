/*
Solution By - Saurabh Verma
Problem-link - https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/
Explanation - 
smallest value x in array can be bloomed after x days.
greatest value y in array can be bloomed after y days.
So, take upper bound as y and lower bound as x
and apply binary search on it.
for every  mid, check whether it can make m bouquets return the number of bouquets that it canMake().
if it make more than k move left otherwise move right.
*/
class Solution {
    public int minDays(int[] bs, int m, int k) {
        if (m == 0) return 0;
        int n = bs.length, l = Integer.MAX_VALUE, r = Integer.MIN_VALUE;
        if (k * m > n) return -1;
        for (int i : bs) {
            l = Math.min(l, i);
            r = Math.max(r, i);
        }
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (canMake(bs, mid, k) >= m) r = mid;
            else l = mid + 1;
        }
        return l;
    }
    
    private int canMake(int[] bs, int mid, int k) {
        int res = 0;
        for (int cnt = 0, i = 0; i < bs.length; i++) {
            if (bs[i] <= mid) cnt++; 
            else cnt = 0;
            if (cnt >= k) {
                res++;
                cnt = 0;
            }
        }
        return res;
    }
}
