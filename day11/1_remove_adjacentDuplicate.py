# created by KUMAR SHANU

# 1. Remove All Adjacent Duplicates In String
# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/


class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = [0]
        for l in S:
            if l == stack[-1]:
                stack.pop(-1)
            else:
                stack.append(l)
        return ''.join(stack[1:])
