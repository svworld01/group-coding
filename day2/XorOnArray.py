class Solution:
    def xorOperation(self, n, start):
        ans=0
        for i in range(n):
            ans^=(start+i*2)
        
        return ans
