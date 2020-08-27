/*
Solution By  - https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/discuss/813725/Java-or-98.6-or-No-Stack-or-ListArray-and-StringBuilder
*/
class Solution {
    public String minRemoveToMakeValid(String s) {
        List<Integer> leftArr = new ArrayList<>();
        char[] chars = s.toCharArray();
        StringBuilder sb = new StringBuilder();
        int validIndex = 0;
        for(int i=0;i<chars.length;i++){
            if(chars[i]=='('){
                leftArr.add(i);
            }else if(chars[i]==')'){
                if(leftArr.size()>0){
                    leftArr.remove(leftArr.size()-1);
                }else{
                    sb.append(s.substring(validIndex,i));
                    validIndex = i+1;   
                }
            }
        }
        for(int index:leftArr){
            if(index>=validIndex){
                sb.append(s.substring(validIndex,index));
                validIndex = index+1;
            }
        }
        sb.append(s.substring(validIndex));
        return sb.toString();
    }
}
