from sortedcontainers import SortedSet

class NumberContainers:
    def __init__(self):
        self.containers = {}
        self.indices = defaultdict(SortedSet)

    def change(self, index: int, number: int) -> None:
        # If there already exists a number at index
        if index in self.containers:
            # Remove the current one
            current = self.containers[index]
            self.indices[current].discard(index)

        # And replace it
        self.containers[index] = number
        self.indices[number].add(index)
    
    def find(self, number: int) -> int:
        # Return the smallest index of a given number, if it exists
        indices = self.indices[number]
        return indices[0] if len(indices) else -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)