# created by KUMAR SHANU

# 2. Make The String Great
# https://leetcode.com/problems/make-the-string-great/


class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for l in s:
            if stack and (ord(stack[-1]) == ord(l) + 32
                          or ord(stack[-1]) == ord(l) - 32):
                stack.pop(-1)
            else:
                stack.append(l)
        return ''.join(stack[:])
