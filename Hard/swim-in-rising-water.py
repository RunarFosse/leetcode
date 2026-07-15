# Author: Runar Fosse
# Time complexity: O(n^2log n)
# Space complexity: O(n^2)

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # Using Union-Find
        n = len(grid)

        # First, generate all edges, with weight being time edge is swimmable
        edges = []
        for i in range(n):
            for j in range(n):
                if i < n - 1:
                    weight = max(grid[i][j], grid[i + 1][j])
                    edges.append(((i, j), (i + 1, j), weight))
                if j < n - 1:
                    weight = max(grid[i][j], grid[i][j + 1])
                    edges.append(((i, j), (i, j + 1), weight))
        
        # Sort the edges by ascending order of weight
        edges.sort(key=lambda e: e[2])

        # Then, in this order, start unioning edges
        uf = UnionFind(n)
        for a, b, weight in edges:
            uf.merge(a, b)

            # If top-left and bottom-right corner end up connected
            if uf.find((0, 0)) == uf.find((n - 1, n - 1)):
                # We have our minimum time
                return weight

        # There might possibly be no edges at all, if so, we can swim at initial time
        return grid[0][0]


# Union-Find implementation
# with union by size and path compression
class UnionFind:
    def __init__(self, n: int):
        self.root = {}
        self.size = {}
        for i in range(n):
            for j in range(n):
                self.root[(i, j)] = (i, j)
                self.size[(i, j)] = 1
    
    def find(self, node: Tuple[int, int]) -> Tuple[int, int]:
        if self.root[node] == node:
            return node
        
        self.root[node] = self.find(self.root[node])
        return self.root[node]
    
    def merge(self, node1: Tuple[int, int], node2: Tuple[int, int]) -> None:
        parent1, parent2 = self.find(node1), self.find(node2)
        if parent1 == parent2:
            return
        
        if self.size[parent2] > self.size[parent1]:
            parent1, parent2 = parent2, parent1
        
        self.root[parent2] = parent1
        self.size[parent1] += self.size[parent2]
