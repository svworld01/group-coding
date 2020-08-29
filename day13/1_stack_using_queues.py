# created by KUMAR SHANU

# 1. Implement Stack using Queues
# https://leetcode.com/problems/implement-stack-using-queues/

# We can Implement stak using two queues.

# Solution 1
"""
Costly pop operation:

    push(x) operation:
        Enqueue x to q1 (assuming size of q1 is unlimited).
    pop() operation:
        One by one dequeue everything except the last element from q1 and enqueue to q2.
        Dequeue the last item of q1, store it in result.
        Swap the names of q1 and q2
        Return the item stored in step 2.

"""

from queue import Queue


class MyStack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
        self.size = 0

    def push(self, x: int) -> None:
        self.size += 1
        self.q1.put(x)

    def pop(self) -> int:
        if self.q1.empty():
            return
        self.size -= 1
        while self.q1.qsize() > 1:
            self.q2.put(self.q1.get())
        result = self.q1.get()
        self.q1, self.q2 = self.q2, self.q1
        return result

    def top(self) -> int:
        if self.q1.empty():
            return
        while self.q1.qsize() > 1:
            self.q2.put(self.q1.get())
        result = self.q1.get()
        self.q2.put(result)
        self.q1, self.q2 = self.q2, self.q1
        return result

    def empty(self) -> bool:
        return self.size == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

# Solution 2
"""
Costly push operation:

    push(x) operation’s step are described below:
        Enqueue x to q2
        One by one dequeue everything from q1 and enqueue to q2.
        Swap the names of q1 and q2
    pop() operation’s function are described below:
        Dequeue an item from q1 and return it.

"""


class MyStack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
        self.size = 0

    def push(self, x: int) -> None:
        self.size += 1
        self.q2.put(x)
        while not self.q1.empty():
            self.q2.put(self.q1.get())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        self.size -= 1
        return self.q1.get()

    def top(self) -> int:
        return self.q1.queue[0]

    def empty(self) -> bool:
        return self.size == 0
