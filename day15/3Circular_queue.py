# created by KUMAR SHANU

# 3. Design Circular Queue
# https://leetcode.com/problems/design-circular-queue


class MyCircularQueue:
    def __init__(self, k: int):

        # initialize queue of size k
        self.q = [None] * k
        self.front = -1
        self.rear = -1
        self.size = k

    def enQueue(self, value: int) -> bool:
        # overflow condition
        if self.isFull():
            print("Queue Overflow!!")
            return False

        # make sure queue is circular
        if self.front == -1:
            self.front = 0
        if self.rear == self.size - 1:
            self.rear = 0
        else:
            self.rear = self.rear + 1
        self.q[self.rear] = value
        return True

    def deQueue(self) -> bool:
        # underflow condition
        if self.isEmpty():
            print("Queue Underflow!!")
            return False
        item = self.q[self.front]

        # only one element
        if self.front == self.rear:
            self.front = -1
            self.rear = -1

        elif self.front == self.size - 1:
            self.front = 0
        else:
            self.front = self.front + 1
        return True

    def Front(self) -> int:

        # get the front element
        if self.isEmpty():
            print("Queue Underflow!!")
            return -1
        return self.q[self.front]

    def Rear(self) -> int:

        # get the rear element
        if self.isEmpty():
            print("Queue Underflow!!")
            return -1
        return self.q[self.rear]

    def isEmpty(self) -> bool:

        # check for queue to be empty
        if self.front == -1 or self.q == []:
            return True
        else:
            return False

    def isFull(self) -> bool:

        # check for queue to be full
        if (self.front == 0
                and self.rear == self.size - 1) or (self.front
                                                    == self.rear + 1):
            return True
        else:
            return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
