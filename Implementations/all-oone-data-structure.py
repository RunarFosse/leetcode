class AllOne:

    def __init__(self):
        # Store a hashmap, containing index per key
        self.indices = defaultdict(int)

        # Store a list of sets, where a key in the set at index i has count i
        self.keys = [set() for _ in range(5 * pow(10, 4))]

        # Store current min and max count for keys
        self.min, self.max = 0, 0

    def inc(self, key: str) -> None:
        # Increment index of key
        self.indices[key] += 1

        # Move key in list of sets
        index = self.indices[key]
        if index > 1:
            self.keys[index - 1].remove(key)
        self.keys[index].add(key)

        # If current index is higher than max, increment it
        if index > self.max:
            self.max = index
        
        # If index is smaller than min, set min to be current index
        if index < self.min:
            self.min = index
        
        # If current index is the smallest in the dataset, increment min too
        if index == self.min + 1 and len(self.keys[index - 1]) == 0:
            self.min = index

    def dec(self, key: str) -> None:
        # Increment index of key
        self.indices[key] -= 1

        # Move key in list of sets
        index = self.indices[key]
        self.keys[index + 1].remove(key)
        if index > 0:
            self.keys[index].add(key)
        
        # If current index is lower than min, decrement it
        if index < self.min:
            self.min = index
        
        # If we decrement min to be 0, iterate list of keys to find
        # index of new min, if it exists
        for i in range(self.max + 1):
            if len(self.keys[i]) == 0:
                continue
            self.min = i
            break
        
        # If current index is the largest in the dataset, decrement max too
        if index == self.max - 1 and len(self.keys[index + 1]) == 0:
            self.max = index

    def getMaxKey(self) -> str:
        # If datastructure is empty, return ""
        if self.max == 0:
            return ""

        # Return a key at the current max index
        return list(self.keys[self.max])[0]

    def getMinKey(self) -> str:
        # If datastructure is empty, return ""
        if self.min == 0:
            return ""

        # Return a key at the current min index
        return list(self.keys[self.min])[0]


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()