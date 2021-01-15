/*
Auther - Saurabh Verma
Problem link - https://leetcode.com/problems/reverse-vowels-of-a-string/
*/
class Solution {
    public String reverseVowels(String s) {
        char[] ch = s.toCharArray();
        int left = 0;
        int right = s.length() - 1;
        HashSet<Character> set = new HashSet<>(Arrays.asList('a','e','i','o','u','A','E','I','O','U'));
        while(left< right){
            if(set.contains(ch[left]) && set.contains(ch[right])){
                char c = ch[left];
                ch[left] = ch[right];
                ch[right] = c;
                left++; right--;
            }else if(set.contains(ch[left])){
                right--;
            }else if(set.contains(ch[right])){
                left++;
            }else{
                left++;
                right--;
            }
        }
        return new String(ch);
    }
}
