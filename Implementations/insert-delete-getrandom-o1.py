class RandomizedSet:

    def __init__(self):
        # We store the values in list, and indices of said values in map
        self.map = {}
        self.list = []

    def insert(self, val: int) -> bool:
        # Return False if already in this set
        if val in self.map:
            return False
        
        # If not, add to the list and index to map
        self.map[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        # Return false if not already in this set
        if val not in self.map:
            return False

        # If not, remove from the set and return true
        # Removing is done through swapping value to be removed,
        # with the value at the back of the list, and popping it.
        # Also remove val's index from map
        current_index, back_index = self.map[val], len(self.list)-1
        self.map[self.list[back_index]] = current_index
        self.list[current_index] = self.list[back_index]
        self.list.pop()
        self.map.pop(val)
        return True

    def getRandom(self) -> int:
        # Randomly sample 1 value from this set
        return sample(self.list, 1)[0]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()