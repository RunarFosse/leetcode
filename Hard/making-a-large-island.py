# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(mn)

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        # Using Union-Find
        m, n = len(grid), len(grid[0])
        max_size = 0

        # Iterate the grid
        uf = UnionFind(m, n)
        for i in range(m):
            for j in range(n):
                # Union all current islands in Union-Find
                if not grid[i][j]:
                    continue
                
                for a, b in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    if 0 <= i+a < m and 0 <= j+b < n and grid[i+a][j+b]:
                        uf.merge((i, j), (i+a, j+b))
                
                # Store current maximum island size
                parent = uf.find(i, j)
                max_size = max(uf.size[parent[0]][parent[1]], max_size)

        # Then iterate the grid again
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    continue

                # And compute the island size if we bridge a zero
                size, seen = 1, set()
                for a, b in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    if 0 <= i+a < m and 0 <= j+b < n and grid[i+a][j+b]:
                        parent = uf.find(i+a, j+b)
                        if parent not in seen:
                            size += uf.size[parent[0]][parent[1]]
                            seen.add(parent)
                    
                # Update maximum island size
                max_size = max(size, max_size)

        # Finally, return the maximum island size
        return max_size


# Union-Find implementation
# with union by rank and path compression
class UnionFind:
    def __init__(self, m, n):
        self.root = [[] for _ in range(m)]
        self.size = [[] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                self.root[i].append((i, j))
                self.size[i].append(1)
    
    def find(self, i, j):
        if self.root[i][j] == (i, j):
            return (i, j)
        
        self.root[i][j] = self.find(*self.root[i][j])
        return self.root[i][j]
    
    def merge(self, node1, node2):
        parent1, parent2 = self.find(*node1), self.find(*node2)
        if parent1 == parent2:
            return
        
        if self.size[parent2[0]][parent2[1]] > self.size[parent1[0]][parent1[1]]:
            parent1, parent2 = parent2, parent1
        
        self.root[parent2[0]][parent2[1]] = parent1
        self.size[parent1[0]][parent1[1]] += self.size[parent2[0]][parent2[1]]