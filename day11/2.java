/*
Auther - Saurabh Verma
*/
class Solution {
    public String makeGood(String s) {
       StringBuilder sb = new StringBuilder(s);
		int i = 0;
		while(i < sb.length()-1){
			if(sb.charAt(i) == sb.charAt(i+1)+32 || sb.charAt(i) == sb.charAt(i+1)-32){
				sb.deleteCharAt(i);
				sb.deleteCharAt(i);
				i = -1;
			}
			i++;
		}
		return sb.toString();
    }
}
