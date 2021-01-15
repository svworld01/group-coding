/*
Problem link - https://leetcode.com/problems/implement-strstr/
*/
class Solution {
    public int strStr(String haystack, String needle) {
        // one line solution--> return haystack.indexOf(needle);
        if (haystack == null || needle == null) {
            return -1;
        }
        if ("".equals(needle)) {
            return 0;
        }
        
        int haystackSize = haystack.length();
        int needleSize = needle.length();
        if (haystackSize < needleSize) {
            return -1;
        }

        if (haystack.equals(needle)) {
            return 0;
        }

        // "abc" "b"
        for (int start = 0; start < haystackSize + 1 - needleSize; ++start) {
            if (haystack.substring(start, start + needleSize).equals(needle)) {
                return start;
            }
        }
        
        return -1;
    }
}
