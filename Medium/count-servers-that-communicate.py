# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(mn)

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        # Using Union-Find
        m, n = len(grid), len(grid[0])

        # Iterate the grid, storing a server in each row / column
        # Also add every server to Union-Find datastructure
        uf = UnionFind()
        self.rows, self.columns = {}, {}
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    if not i in self.rows:
                        self.rows[i] = (i, j)
                    if not j in self.columns:
                        self.columns[j] = (i, j)
                    
                    # Connect this server to all neighbours in Union-Find
                    uf.merge((i, j), self.rows[i])
                    uf.merge((i, j), self.columns[j])
        
        # Return number of servers with at least one partner
        return sum(1 if uf.size[node] > 1 else 0 for node in uf.root.values())

# Union-Find implementation
# with union by rank and path compression
class UnionFind:
    def __init__(self):
        self.root, self.size = {}, {}
    
    def find(self, node):
        if node not in self.root:
            self.root[node] = node
            self.size[node] = 1

        if self.root[node] == node:
            return node
        
        self.root[node] = self.find(self.root[node])
        return self.root[node]
    
    def merge(self, node1, node2):
        parent1, parent2 = self.find(node1), self.find(node2)
        if parent1 == parent2:
            return
        
        if self.size[parent2] > self.size[parent1]:
            parent1, parent2 = parent2, parent1
        
        self.root[parent2] = parent1
        self.size[parent1] += self.size[parent2]