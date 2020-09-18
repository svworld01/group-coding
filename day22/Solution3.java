/*
Solution By - Saurabh Verma
*/
class Solution {
    public int lastStoneWeight(int[] stones) {
        if(stones.length == 1) 
            return stones[0];
        int n = stones.length;
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        for(int stone : stones) 
            pq.add(stone);
        
        while(pq.size() > 1) {
            int  z=Math.abs(pq.poll()-pq.poll());
            if(z!= 0) pq.add(z);
        }
        if(pq.size() == 0) return 0;
        return pq.poll();
    }
}
