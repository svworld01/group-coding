# created by KUMAR SHANU

# 1. Min Stack
# https://leetcode.com/problems/min-stack/


# Solution 1
class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stk = []

    def push(self, x: int) -> None:
        self.stk.append(x)

    def pop(self) -> None:
        self.stk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return min(self.stk)


# Solution 2
"""
Optimal Solution.
getMin() -> in O(1) time
"""


class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.min = []

    def push(self, x: int) -> None:
        if self.min == [] or x <= self.min[-1]:
            self.min.append(x)
        else:
            self.min.append(self.min[-1])
        self.data.append(x)

    def pop(self) -> None:
        self.data.pop(-1)
        self.min.pop(-1)

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.min[-1]
