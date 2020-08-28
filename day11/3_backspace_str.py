# created by KUMAR SHANU

# 3. Backspace String Compare
# https://leetcode.com/problems/backspace-string-compare/


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        a1, a2 = [], []
        for i in range(len(S)):
            if S[i] == '#':
                if a1 == []:
                    pass
                else:
                    a1.pop()
            else:
                a1.append(S[i])

        for i in range(len(T)):
            if T[i] == '#':
                if a2 == []:
                    pass
                else:
                    a2.pop()
            else:
                a2.append(T[i])
        return a1 == a2
