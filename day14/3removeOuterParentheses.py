# created by KUMAR SHANU

# 3. Remove Outermost Parentheses
# https://leetcode.com/problems/remove-outermost-parentheses/


class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        s = list(S)
        l, r = 0, 0
        for i in range(len(s)):
            if s[i] == '(':
                l += 1
            elif s[i] == ')':
                r += 1
            if l == r:
                s[i] = '#'
                s[i - (l + r) + 1] = '#'
                l, r = 0, 0
        return ''.join(s).replace('#', '')
