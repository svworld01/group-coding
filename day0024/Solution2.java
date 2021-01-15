/*
Solution By - Saurabh Verma
*/
class Solution {
    public boolean carPooling(int[][] trips, int capacity) {
        TreeMap<Integer, Integer> map = new TreeMap<>();
        
        for (int[] trip : trips) {
            map.put(trip[1], map.getOrDefault(trip[1], 0) + trip[0]);
            map.put(trip[2], map.getOrDefault(trip[2], 0) - trip[0]);
        }
        int countPassengers = 0;
        for (int value : map.values()) {
            countPassengers += value;
            if (countPassengers > capacity) {
                return false;
            }
        }
        return true;
    }
}
