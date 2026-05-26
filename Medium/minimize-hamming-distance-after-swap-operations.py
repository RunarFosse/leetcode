class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        # Using Union-Find
        n = len(target)

        # Iterate all allowed swaps, storing possible "swap" groups as unions
        groups = UnionFind(n)
        for a, b in allowedSwaps:
            groups.merge(a, b)
        
        # Iterate the source array
        elements = defaultdict(lambda: defaultdict(int))
        for i in range(n):
            # Storing available elements per swap group
            group = groups.find(i)
            elements[group][source[i]] += 1
        
        # At last, iterate the target array
        distance = 0
        for i in range(n):
            # If the wanted character is available in the swap group
            group = groups.find(i)
            if elements[group][target[i]] > 0:
                # Use one
                elements[group][target[i]] -= 1
            else:
                # Otherwise, increment Hamming distance
                distance += 1
        
        # Finally, return this minimum Hamming distance after swaps
        return distance


# Union-Find implementation
# with union by rank and path compression
class UnionFind:
    def __init__(self, size: int):
        self.root = []
        self.size = []
        for i in range(size):
            self.root.append(i)
            self.size.append(1)
    
    def find(self, node: int) -> int:
        if self.root[node] == node:
            return node
        
        self.root[node] = self.find(self.root[node])
        return self.root[node]
    
    def merge(self, node1: int, node2: int) -> None:
        parent1, parent2 = self.find(node1), self.find(node2)
        if parent1 == parent2:
            return
        
        if self.size[parent2] > self.size[parent1]:
            parent1, parent2 = parent2, parent1
        
        self.root[parent2] = parent1
        self.size[parent1] += self.size[parent2]
