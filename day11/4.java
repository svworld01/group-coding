/*
Auther - Saurabh Verma
*/
class Solution {
    public int minAddToMakeValid(String S) {
        int left=0, right = 0;
        for(char c: S.toCharArray()){
            if(c == ')'){
                if(left == 0)
                    right++;
                else
                    left--;
            }
            else
                left++;
        }
        return left + right;
    }
}
