# created by KUMAR SHANU

# 5. Minimum Remove to Make Valid Parentheses
# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if stack == []:
                    s[i] = '#'
                else:
                    stack.pop(-1)
        for i in range(len(stack)):
            s[stack[-1]] = '#'
            stack.pop(-1)
        return ''.join(s).replace('#', '')
