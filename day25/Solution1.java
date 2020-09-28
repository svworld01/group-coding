/*
Solution By - Saurabh Verma
Approach - Use Backtracking (Brute Force)
*/
class Solution {
    public List<Integer> splitIntoFibonacci(String S) {
        LinkedList<Integer> list = new LinkedList<>();
        solve(S, 0, list );
        return list;        
    }
    public boolean solve(String s, int i, LinkedList<Integer> list){
        if(list.size() > 2){
            int len = list.size();
            if(list.get(len-1) != list.get(len-2) + list.get(len-3))
                return false;
        }
        if(i >= s.length())
            return list.size() >= 3;
        int num = 0;
        int index = i;
        while(index < s.length()){
            int value = num * 10 + (s.charAt(index++) - '0');
            if(index == i+2 && value < 10 || value / 10 != num)
                return false;
            num = value;
            list.add(num);
            if(solve(s, index, list))
                return true;
            list.removeLast();
        }
        return false;
    }
}
