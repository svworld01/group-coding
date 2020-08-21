/********auther---Akash******/



public class Solution {
    public char findTheDifference(String s, String t) {
        int res = 0;
        for (int i = 0; i < s.length(); i ++) {
            res = res - s.charAt(i);
            res = res + t.charAt(i);
        }
        res = res + t.charAt(t.length() - 1);
        return (char)res;
    }
}
