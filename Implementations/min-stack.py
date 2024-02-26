class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []
        
    def push(self, val: int) -> None:
        # Append value to stack
        self.stack.append(val)

        # and to minStack as well if value is smaller than current top
        if not self.minStack or self.minStack[-1] >= val:
            self.minStack.append(val)

    def pop(self) -> None:
        # Pop value from stack
        val = self.stack.pop()

        # If it is equal to top of minStack, pop that as well
        if self.minStack and val == self.minStack[-1]:
            self.minStack.pop()

    def top(self) -> int:
        # Retrieve top of stack
        return self.stack[-1]

    def getMin(self) -> int:
        # Retrieve top of minStack
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()