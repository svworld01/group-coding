/*
Problem Link - https://www.interviewbit.com/problems/gray-code/
The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

00 - 0
01 - 1
11 - 3
10 - 2
There might be multiple gray code sequences possible for a given n.
Return any such sequence.
*/
public class Solution {
    public ArrayList<Integer> grayCode(int a) {
        ArrayList<Integer> res = new ArrayList<Integer>();
        solve(a, res);
        return res;
    }
    private void solve(int a, ArrayList<Integer> res){
        if( a == 1 ){
            res.add(0);
            res.add(1);
            return;
        }
        solve(a-1, res);
        int n = res.size();
        for(int i = n-1; i>=0; i--){
            int tmp = res.get(i);
            tmp = tmp | (1 << (a-1));
            res.add(tmp);
        }
    }
}
