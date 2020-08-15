# created by KUMAR SHANU

# 3. Implement strStr()
# https://leetcode.com/problems/implement-strstr/


"""
Approach : Two Pointers solution
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # find length of both strings
        n = len(haystack)
        m = len(needle)
        
        # pointers i -> haystack
        # j -> needle
        i,j = 0, 0
        
        if m == 0:
            return 0
        
        # scan string until its lenght is greater than or equal to lenght of the needle string
        while i<n and n-i+1 >= m:
        
            if haystack[i] == needle[j]:
                k = i
                
                # move the pointers
                while j<m and i<n and haystack[i] == needle[j]:
                    i += 1
                    j += 1
                    
                # if we found substring
                if j == m:
                    return k
                
                # otherwise continue to scan and repoint the pointer to the starting of needle string    
                i = k + 1
                j = 0
                
            else:
                i += 1
        
        # return -1 if we doesn't find substring in haystack          
        return -1
 
