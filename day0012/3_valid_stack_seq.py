# created by KUMAR SHANU

# 3. Validate Stack Sequences
# https://leetcode.com/problems/validate-stack-sequences/


class Solution:
    def validateStackSequences(self, pushed: List[int],
                               popped: List[int]) -> bool:
        i = 0
        stack = []
        for n in pushed:
            stack.append(n)

            while stack and i < len(popped) and stack[-1] == popped[i]:
                stack.pop(-1)
                i += 1
        return i == len(popped)
