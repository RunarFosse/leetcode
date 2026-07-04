# Author: Runar Fosse
# Time complexity: O(m + n)
# Space complexity: O(n)

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # Using Union-Find

        # Add all edges to Union-Find datastructure
        uf = UnionFind(n)
        for a, b, weight in roads:
            uf.merge(a - 1, b - 1, weight)
        
        # Finally, get the minimum score to get to city n
        return uf.scores[uf.find(n - 1)]

# Union-Find implementation
# with union by rank and path compression
class UnionFind:
    def __init__(self, size):
        self.root = []
        self.size = []
        self.scores = []
        for i in range(size):
            self.root.append(i)
            self.size.append(1)
            self.scores.append(1e9)
    
    def find(self, node: int) -> int:
        if self.root[node] == node:
            return node
        
        self.root[node] = self.find(self.root[node])
        return self.root[node]
    
    def merge(self, node1: int, node2: int, weight: int) -> None:
        parent1, parent2 = self.find(node1), self.find(node2)

        if self.size[parent2] > self.size[parent1]:
            parent1, parent2 = parent2, parent1

        # Update the score to be the minimum of either subcomponent + new edge weight
        self.scores[parent1] = min(weight, self.scores[parent1], self.scores[parent2])

        if parent1 == parent2:
            return
        
        self.root[parent2] = parent1
        self.size[parent1] += self.size[parent2]

# Because we can traverse every path and city any number of times, the minimum score
# to get from city 1 to city n will be equal to the minimum edge weight in the
# connected component containing both city 1 and city n, making the solution trivial.