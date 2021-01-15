/*
Auther - Saurabh Verma
Problem link - https://leetcode.com/problems/assign-cookies/
*/
//SOLUTION 1
class Solution {
    public int findContentChildren(int[] g, int[] s) {
        Arrays.sort(g);
        Arrays.sort(s);
        int count =  0;
        int i = 0;
        int j = 0;
        while(i<g.length){
            
            while(j<s.length){
                if(s[j++] >= g[i]){
                    count++;
                    break;
                }    
            }
            if(j == s.length)
                break;
            i++;
            
        }
        return count;
    }
}
//SOLUTION 2
class Solution {
    public int findContentChildren(int[] g, int[] s) {
        Arrays.sort(g);
        Arrays.sort(s);
        int i = g.length - 1;
        int j = s.length - 1;
        while(i >=0 && j >= 0){
            if (g[i] <= s[j]) 
                j--;
            i--;
        }
        return s.length - j - 1;
    }
}
