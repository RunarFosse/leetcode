class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []

    def push(self, x: int) -> None:
        # Only add to stack if it isn't full
        if len(self.stack) < self.maxSize:
            self.stack.append(x)
        
    def pop(self) -> int:
        # If stack is empty, return -1
        if not self.stack:
            return -1
            
        # If not, pop the top element
        return self.stack.pop()

    def increment(self, k: int, val: int) -> None:
        # If k is bigger than current stack, increment every value
        k = min(k, len(self.stack))

        # Increment the k bottom elements by val
        for i in range(k):
            self.stack[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)