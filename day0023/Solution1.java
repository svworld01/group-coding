/*
Solution By - Saurabh Verma
*/
//SOLUTION 1
class Solution {
    public boolean canConstruct(String s, int k) {
        if(k > s.length())
            return false;
        Map<Character, Integer> m = new HashMap<>();
        for(char c: s.toCharArray())
            m.put(c, m.getOrDefault(c, 0)+1);
        int odd = 0;
        for(Map.Entry<Character, Integer> e: m.entrySet()){
            if((e.getValue() & 1) == 1)
                odd++;
            if(odd > k)
                return false;
        }
        return true;
    }
}
//SOLUTION 2
class Solution {
    public boolean canConstruct(String s, int k) {
        if(s.length() < k) {
            return false;
        }
        Set<Character> set = new HashSet<>();
        for(int i = 0; i < s.length(); i++) {
            if(set.contains(s.charAt(i))) {
                set.remove(s.charAt(i));
            } else {
                set.add(s.charAt(i));
            }
        }
        return set.size() <= k;
    }
}
