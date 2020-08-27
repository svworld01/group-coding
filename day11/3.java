/*
Auther - Saurabh Verma
*/
class Solution {
     public boolean backspaceCompare(String S, String T) {
        Stack<Character> s1=new Stack<>();
        Stack<Character> s2=new Stack<>();
       
        for(char c: S.toCharArray()){
            if(c == '#'){
                if(!s1.isEmpty())
                s1.pop();
            }
            else
                s1.push(c);
        }
         for(char c: T.toCharArray()){
            if(c == '#'){
                if(!s2.isEmpty())
                s2.pop();
            }
            else
                s2.push(c);
        }
       return s1.toString().equals(s2.toString());
    }
}
