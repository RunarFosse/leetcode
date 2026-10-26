# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(mn)

class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        # Using Union-Find
        m, n = len(grid), len(grid[0])

        # Store island values in a Union-Find datastructure
        uf = UnionFind(m, n, grid)

        # Iterate every cell
        for i in range(m):
            for j in range(n):
                if not grid[i][j]:
                    continue
                
                # Union cell together with every neighbour island cell
                for a, b in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    if 0 <= i + a < m and 0 <= j + b < n and grid[i + a][j + b]:
                        uf.union((i, j), (i + a, j + b))
        
        # Then, iterate every island
        islands = 0
        for i in range(m):
            for j in range(n):
                if uf.find((i, j)) == (i, j) and not uf.value[i][j] % k:
                    # Counting the islands with a total value divisible by k
                    islands += 1

        return islands


class UnionFind:
    def __init__(self, m: int, n: int, grid: List[List[int]]):
        self.root = [[(i, j) if grid[i][j] else None for j in range(n)] for i in range(m)]
        self.size = [[1 for j in range(n)] for i in range(m)]
        self.value = grid
    
    def find(self, node: Tuple[int, int]) -> Tuple[int, int]:
        if node is None:
            return None
        
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
        self.value[i1][j1] += self.value[i2][j2]
