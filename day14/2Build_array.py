# created by KUMAR SHANU

# 2. Build an Array With Stack Operations
# https://leetcode.com/problems/build-an-array-with-stack-operations


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        #r = range(1,n+1)
        val = 1
        for i in range(len(target)):
            while val < target[i]:
                ans += ["Push", "Pop"]
                val += 1
            ans += ["Push"]
            val += 1
        return ans
