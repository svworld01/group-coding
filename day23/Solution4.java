/*
Solution By - Saurabh Verma
*/
class Solution {
    public int minSetSize(int[] arr) {
        HashMap<Integer, Integer> map = new HashMap<>();
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        for(int i: arr)
            map.put(i, map.getOrDefault(i, 0)+1);
        for(Map.Entry<Integer,Integer> e: map.entrySet())
            pq.add(e.getValue());
        int half = arr.length >> 1;
        int sum = 0;
        int count = 0;
        while(sum <half){
            sum += pq.poll();
            count++;
        }
        return count;
    }
}
