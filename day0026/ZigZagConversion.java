/*
Problem Link - https://leetcode.com/problems/zigzag-conversion
*/
class Solution {
    public String convert(String s, int numRows) {
        if(numRows == 1) return s;
        List<StringBuilder> ls = new ArrayList<>();
        for(int i=0; i<Math.min(numRows, s.length()); i++){
            ls.add(new StringBuilder());
        }
        
        int curRow = 0;
        boolean goingDown = false;
        
        for(char c: s.toCharArray()){
            ls.get(curRow).append(c);
            if(curRow == 0 || curRow == numRows - 1)
                goingDown = !goingDown;
            
            curRow += goingDown ? 1:-1;
        }
        
        StringBuilder res = new StringBuilder();
        for(StringBuilder sb: ls){
            res.append(sb);
        }
        return res.toString();
        
    }
}
