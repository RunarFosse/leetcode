# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Using Union-Find
        n = len(edges)

        uf = UnionFind(n)
        for a, b in edges:
            # If merging fails, edges make a cycle
            if not uf.merge(a, b):
                return [a, b]


# Union-Find implementation
# with union by rank and path compression
class UnionFind:
    def __init__(self, size):
        self.root = []
        self.size = []
        for i in range(size+1):
            self.root.append(i)
            self.size.append(1)
    
    def find(self, node):
        if self.root[node] == node:
            return node
        
        self.root[node] = self.find(self.root[node])
        return self.root[node]
    
    def merge(self, node1, node2):
        parent1, parent2 = self.find(node1), self.find(node2)
        if parent1 == parent2:
            return False
        
        if self.size[parent2] > self.size[parent1]:
            parent1, parent2 = parent2, parent1
        
        self.root[parent2] = parent1
        self.size[parent1] += self.size[parent2]
        return True