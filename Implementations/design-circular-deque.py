class MyCircularDeque:

    def __init__(self, k: int):
        self.list = [0] * k
        self.k, self.length = k, 0
        self.front, self.back = 0, 1

    def insertFront(self, value: int) -> bool:
        # If list is full, we cannot insert
        if self.isFull():
            return False
        
        # If not, insert at front and move pointer
        self.list[self.front] = value
        self.front = (self.front - 1) % self.k
        self.length += 1
        return True

    def insertLast(self, value: int) -> bool:
        # If list is full, we cannot insert
        if self.isFull():
            return False
        
        # If not, insert at back and move pointer
        self.list[self.back] = value
        self.back = (self.back + 1) % self.k
        self.length += 1
        return True

    def deleteFront(self) -> bool:
        # If the list is empty, we cannot delete
        if self.isEmpty():
            return False
        
        # If not, delete from front by moving pointer
        self.front = (self.front + 1) % self.k
        self.length -= 1
        return True

    def deleteLast(self) -> bool:
        # If the list is empty, we cannot delete
        if self.isEmpty():
            return False
        
        # If not, delete from back by moving pointer
        self.back = (self.back - 1) % self.k
        self.length -= 1
        return True

    def getFront(self) -> int:
        # If the queue is empty, return -1
        if self.isEmpty():
            return -1

        # If not, get the item at the front of the queue
        return self.list[(self.front + 1) % self.k]

    def getRear(self) -> int:
        # If the queue is empty, return -1
        if self.isEmpty():
            return -1

        # If not, get the item at the back of the queue
        return self.list[(self.back - 1) % self.k]

    def isEmpty(self) -> bool:
        # The queue is empty if the length of the queue is 0
        return self.length == 0
        
    def isFull(self) -> bool:
        # The queue is full if the length of the queue is k
        return self.length == self.k


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