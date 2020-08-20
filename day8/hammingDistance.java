***************************Auther---Akash(The Robust Coder)********************8

/*

class Solution {
    public int hammingDistance(int x, int y) {
        
        int hd=x^y;
        return Integer.bitCount(hd);
    }
}


*/

class Solution {
    public int hammingDistance(int x, int y) {
        int count=0;
        int hd=x^y;
        while(hd!=0) { 
        count +=hd & 1; 
        hd >>= 1; 
    } 
    return count; 
    }
}
