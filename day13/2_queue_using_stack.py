# created by KUMAR SHANU

# 2. Implement Queue using Stacks
# https://leetcode.com/problems/implement-queue-using-stacks

# Solution
"""
We can implement queue using two stacks.
"""


class MyQueue:
    def __init__(self):
        # stack 1
        self.s1 = []
        # stack 2
        self.s2 = []
        self.size = 0

    def push(self, x: int) -> None:
        self.size += 1
        # pop everything from stack 1 and put into stack 2
        while self.s1 != []:
            self.s2.append(self.s1.pop(-1))

        # push the 'x' into stack 1
        self.s1.append(x)

        # move everything back into stack 1
        while self.s2 != []:
            self.s1.append(self.s2.pop(-1))

    def pop(self) -> int:
        self.size -= 1
        return self.s1.pop(-1)

    def peek(self) -> int:
        return self.s1[-1]

    def empty(self) -> bool:
        return self.size == 0
