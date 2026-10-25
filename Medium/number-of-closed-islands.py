# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(mn)

class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        # Using Union-Find
        m, n = len(grid), len(grid[0])

        # Create a Union-Find datastructure to hold disjoint islands
        uf = UnionFind(m, n)

        # Count the number of disjoint islands
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    continue

                # If we are at an island, join with neighbour island cells
                for a, b in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    if 0 <= i + a < m and 0 <= j + b < n and not grid[i + a][j + b]:
                        uf.union((i, j), (i + a, j + b))
        
        # Find every island at the rim of the grid
        opened = set()
        for i in range(m):
            opened.update([uf.find((i, 0)), uf.find((i, n - 1))])
        for j in range(n):
            opened.update([uf.find((0, j)), uf.find((m - 1, j))])
        
        # Then, find every disjoint closed island inside the grid
        closed = set()
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                island = uf.find((i, j))
                if not grid[i][j] and island not in opened:
                    closed.add(island)
        
        # Finally, return the number of these closed islands on the grid
        return len(closed)


class UnionFind:
    def __init__(self, m: int, n: int):
        self.root = [[(i, j) for j in range(n)] for i in range(m)]
        self.size = [[1 for j in range(n)] for i in range(m)]
    
    def find(self, node: Tuple[int, int]) -> Tuple[int, int]:
        i, j = node
        if node == self.root[i][j]:
            return node
        
        self.root[i][j] = self.find(self.root[i][j])
        return self.root[i][j]
    
    def union(self, node1: Tuple[int, int], node2: Tuple[int, int]) -> None:
        (i1, j1), (i2, j2) = self.find(node1), self.find(node2)
        if (i1, j1) == (i2, j2):
            return
        
        if self.size[i1][j1] < self.size[i2][j2]:
            (i1, j1), (i2, j2) = (i2, j2), (i1, j1)
        
        self.root[i2][j2] = (i1, j1)
        self.size[i1][j1] += self.size[i2][j2]
