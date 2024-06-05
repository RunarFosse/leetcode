# Author: Runar Fosse
# Time complexity: O((nm)^2)
# Space complexity: O(nm)

class Solution:
    # Declare possible moves for each cell
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        # Using DFS
        self.n, self.m = len(grid), len(grid[0])
        self.grid = grid

        # Start DFS from each starting position
        max_gold = 0
        for i in range(self.n):
            for j in range(self.m):
                max_gold = max(self.dfs(i, j), max_gold)
        
        # Return maximum gold from path
        return max_gold
    
    def dfs(self, i: int, j: int) -> int:
        # Ensure we are at a path is valid and current cell contains gold
        invalid_cell = (i < 0 or i >= self.n or j < 0 or j >= self.m)
        if invalid_cell or self.grid[i][j] == 0:
            return 0
        
        # Collect gold, and override value preventing iteration of cell twice
        gold = self.grid[i][j]
        self.grid[i][j] = 0

        # Perform DFS
        next_gold = max(self.dfs(i+y, j+x) for (y, x) in self.moves)

        # Reassign picked up gold back and return
        self.grid[i][j] = gold
        return gold + next_gold
        