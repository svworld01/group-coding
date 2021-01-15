/*
Auther - Saurabh Verma
Aprroach 1: use map to count frequncy and return all whose frequency is more than 1.
*/
public class Solution{
public List<String> findRepeatedDnaSequences(String s) {
    if (s == null || s.isBlank())
		return Collections.emptyList();
    Map<String, Integer> map = new HashMap<>();
	for (int i = 0; i < s.length() - 9; i++) {
		String x = s.substring(i, i + 10);
		map.merge(x, 1, (a, b) -> a + 1);
	}
	map.entrySet().removeIf(x -> x.getValue() < 2);
    
	return new ArrayList<>(map.keySet());
}
}
/*
Approach 2: Use two sets to store first occurance and repeated substring of size 10.
if seen first time add it to set1 otherwise add into set2
*/
public class Solution{
    public List<String> findRepeatedDnaSequences(String s) {
        Set seen = new HashSet(); 
        Set repeated = new HashSet();
        for (int i = 0; i + 9 < s.length(); i++) {
            String tmp = s.substring(i, i + 10);
            if (!seen.add(tmp))
                repeated.add(tmp);
        }
        return new ArrayList(repeated);
    }
}
