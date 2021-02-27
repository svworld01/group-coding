class Solution {
    public int romanToInt(String s) {
        int result = 0;
        int prev = 0;
        for(int i=s.length() -1; i>=0; i--){
            int value = getValue(s.charAt(i));
            if(prev > value)
                result -= value;
            else
                result += value;
            prev = value;
        }
        return result;
    }
    public int getValue(char c){
        if (c == 'I') return 1;
        else if (c == 'V') return 5;
        else if (c == 'X') return 10;
        else if (c == 'L') return 50;
        else if (c == 'C') return 100;
        else if (c == 'D') return 500;
        else if (c == 'M') return 1000;
        else return 0;
    }
}