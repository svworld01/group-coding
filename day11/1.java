/*
Auther - Saurabh Verma
*/

class Solution {
    public String removeDuplicates(String S) {
        Stack<Character> stk = new Stack<>();
        for(char c: S.toCharArray()){
            if(stk.isEmpty())
                stk.push(c);
            else if(stk.peek() == c)
                stk.pop();
            else
                stk.push(c);
        }
        String res = "";
        while(!stk.isEmpty()){
            res = stk.pop() + res;
        }
        return res;
    }
}
