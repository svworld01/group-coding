# created by KUMAR SHANU

# 4. Baseball Game
# https://leetcode.com/problems/baseball-game/


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        for i in ops:
            if stack and i == '+':
                points = stack[-1] + stack[-2]
                stack.append(points)
            elif stack and i == 'D':
                points = 2 * stack[-1]
                stack.append(points)
            elif stack and i == 'C':
                stack.pop(-1)
            else:
                stack.append(int(i))
        return sum(stack)
