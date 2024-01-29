class MyQueue:

    def __init__(self):
        # Initialize two stacks, one for holding inputs (LIFO)
        # and other for holding outputs (LLIFO == FIFO)
        self.inputStack = []
        self.outputStack = []

    def push(self, x: int) -> None:
        # Add element to the input stack
        self.inputStack.append(x)

    def pop(self) -> int:
        # If the output stack is empty, refill it from the input stack
        if not self.outputStack:
            while self.inputStack:
                self.outputStack.append(self.inputStack.pop())
        
        # Pop the last element of the output stack
        return self.outputStack.pop()

    def peek(self) -> int:
        # If the output stack is empty, refill it from the input stack
        if not self.outputStack:
            while self.inputStack:
                self.outputStack.append(self.inputStack.pop())
        
        # Peek the last element of the output stack
        return self.outputStack[-1]

    def empty(self) -> bool:
        # Verify that the total size is empty
        size = len(self.inputStack) + len(self.outputStack)
        return not size


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()