# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(mn)

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        # Using Union-Find

        # Store connected land in a Union-Find datastructure
        grid, uf = [[False] * col for _ in range(row)], UnionFind(row, col)

        # With special nodes denoting top and bottom connection
        top, bottom = (row, 0), (row, 1)

        # Iterate the days in reverse
        days = [(day, (i - 1, j - 1)) for day, (i, j) in enumerate(cells)]
        for day, (i, j) in reversed(days):
            # Marking flooded land as dry
            grid[i][j] = True

            # Check neighbouring land
            for a, b in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if i + a < 0 or i + a >= row or j + b < 0 or j + b >= col:
                    continue
                
                # If they are dry, union them together
                if grid[i + a][j + b]:
                    uf.merge((i, j), (i + a, j + b))
            
            # If the current cell is in the top or bottom row, mark them accordingly
            if i == 0:
                uf.merge((i, j), top)
            if i == row - 1:
                uf.merge((i, j), bottom)
            
            # Finally, if there is a valid path between, return the day
            if uf.find(top) == uf.find(bottom):
                return day

        
# Union-Find implementation
# with union by rank and path compression
class UnionFind:
    def __init__(self, m: int, n: int):
        self.root = [[(i, j) for j in range(n)] for i in range(m)]
        self.size = [[1] * n for _ in range(m)]

        # Special value for top and bottom connection
        self.root.append([(m, 0), (m, 1)])
        self.size.append([1, 1])
    
    def find(self, node: (int, int)) -> (int, int):
        (i, j) = node
        if self.root[i][j] == (i, j):
            return (i, j)
        
        self.root[i][j] = self.find(self.root[i][j])
        return self.root[i][j]
    
    def merge(self, node1: (int, int), node2: (int, int)):
        parent1, parent2 = self.find(node1), self.find(node2)
        if parent1 == parent2:
            return
        
        if self.size[parent2[0]][parent2[1]] > self.size[parent1[0]][parent1[1]]:
            parent1, parent2 = parent2, parent1
        
        self.root[parent2[0]][parent2[1]] = parent1
        self.size[parent1[0]][parent1[1]] += self.size[parent2[0]][parent2[1]]