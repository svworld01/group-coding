# created by KUMAR SHANU

#4. Design Circular Deque
# https://leetcode.com/problems/design-circular-deque


class MyCircularDeque:
    def __init__(self, k: int):
        # initialize queue of size k
        self.q = [None] * k
        self.front = -1
        self.rear = -1
        self.size = k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            print("Queue Overflow!!")
            return False
        if self.front == -1:
            self.front = 0
            self.rear = 0
        elif self.front == 0:

            self.front = self.size - 1
        else:
            self.front -= 1
        self.q[self.front] = value
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            print("Queue Overflow!!")
            return False
        if self.front == -1:
            self.front = 0
            self.rear = 0
        elif self.rear == self.size - 1:
            self.rear = 0
        else:
            self.rear += 1
        self.q[self.rear] = value
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            print("Queue Underflow!!")
            return False
        item = self.q[self.front]

        # only one item
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        elif self.front == self.size - 1:
            self.front = 0
        else:
            self.front += 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            print("Queue Underflow!!")
            return False
        item = self.q[self.rear]

        # only one item
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        elif self.rear == 0:
            self.rear = self.size - 1
        else:
            self.rear -= 1
        return True

    def getFront(self) -> int:

        # get the front element
        if self.isEmpty():
            print("Queue Underflow!!")
            return -1
        return self.q[self.front]

    def getRear(self) -> int:

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


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
