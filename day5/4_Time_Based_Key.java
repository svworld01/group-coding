/*
  Auther - Saurabh Verma
  Problem link - https://leetcode.com/problems/time-based-key-value-store/
  Approach - Map and binarySearch
 
*/
class TimeMap {
    Map<String, List<Pair<Integer, String>>> M;
    //def Pair class
    class Pair<K, V>{
        K key;
        V value;
        Pair(K k,V v){
            key = k;
            value = v;
        }
        K getKey(){
            return key;
        }
        V getValue(){
            return value;
        }
    }
    public TimeMap() {
        M = new HashMap();
    }

    public void set(String key, String value, int timestamp) {
        if (!M.containsKey(key))
            M.put(key, new ArrayList<Pair<Integer, String>>());

        M.get(key).add(new Pair(timestamp, value));
    }

    public String get(String key, int timestamp) {
        if (!M.containsKey(key)) return "";

        List<Pair<Integer, String>> A = M.get(key);
        int i = Collections.binarySearch(A, new Pair<Integer, String>(timestamp, "{"),
                (a, b) -> Integer.compare(a.getKey(), b.getKey()));

        if (i >= 0)
            return A.get(i).getValue();
        else if (i == -1)
            return "";
        else
            return A.get(-i-2).getValue();
    }
}
