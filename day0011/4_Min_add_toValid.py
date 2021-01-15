# created by KUMAR SHANU

# 4. Minimum Add to Make Parentheses Valid
# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/


class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        stack = []
        for l in S:
            if stack and (stack[-1] == '(' and l == ')'):
                stack.pop(-1)
            else:
                stack.append(l)
        return len(stack)
