/*
Solution By - Saurabh Verma
*/
class Solution {
    public int minimumSwap(String s1, String s2) {
        int xy = 0;
        int yx = 0;
        int swap = 0;
        for(int i=0; i<s1.length(); i++){
            if(s1.charAt(i) != s2.charAt(i)){
                if(s1.charAt(i) == 'x')
                    xy++;
                else
                    yx++;
            }
        }
        swap = xy/2 + yx/2;
        xy %= 2; yx %= 2;
        if(xy != yx) return -1;
        return swap + 2*xy;
    }
}
