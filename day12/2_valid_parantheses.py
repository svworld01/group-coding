# created by KUMAR SHANU

# 2. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/


class Solution:
    def isValid(self, s: str) -> bool:
        stack = ['$']
        for l in s:

            if l == ')':
                if stack[-1] == '(':
                    stack.pop(-1)
                else:
                    stack.append(l)

            elif l == '}':
                if stack[-1] == '{':
                    stack.pop(-1)
                else:
                    stack.append(l)

            elif l == ']':
                if stack[-1] == '[':
                    stack.pop(-1)
                else:
                    stack.append(l)

            else:
                stack.append(l)

        return stack[1:] == []
