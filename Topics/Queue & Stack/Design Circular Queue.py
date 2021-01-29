class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [-1] * k
        self.head = self.tail = -1

    def enQueue(self, value: int) -> bool:
        if self.head == -1:
            self.q[0] = value
            self.head = 0
            self.tail = 0
            return True
        elif self.tail == len(self.q) - 1:
            if self.head == 0:
                return False
            else:
                self.q[0] = value
                self.tail = 0
                return True
        elif self.q[self.head] == -1:
            self.q[self.head] = value
            return True
        else:
            if self.tail + 1 == self.head:
                return False
            else:
                self.tail += 1
                self.q[self.tail] = value
                return True

    def deQueue(self) -> bool:
        if self.head == -1 or self.q[self.head] == -1:
            return False
        if self.head == self.tail:
            self.q[self.head] = -1
        elif self.head == len(self.q) - 1:
            self.q[-1] = -1
            self.head = 0
        else:
            self.q[self.head] = -1
            self.head += 1
        return True

    def Front(self) -> int:
        if self.q[self.head] == -1:
            return -1
        return self.q[self.head]

    def Rear(self) -> int:
        if self.q[self.tail] == -1:
            return -1
        return self.q[self.tail]

    def isEmpty(self) -> bool:
        return self.q[self.head] == -1

    def isFull(self) -> bool:
        return (self.tail == len(self.q) - 1 and self.head == 0) or self.tail + 1 == self.head

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
