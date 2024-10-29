# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(mn)

class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        # Using dynamic programming
        self.grid, self.n, self.m = grid, len(grid), len(grid[0])
        return max(self.opt(i, 0) for i in range(self.n))
    
    @functools.cache
    def opt(self, i: int, j: int) -> int:
        # Declare the neighbourhood of possible cells to move to
        neighbourhood = [(i-1, j+1), (i, j+1), (i+1, j+1)]

        # Compute the best neighbour to move to
        max_moves = 0
        for k, l in neighbourhood:
            # If the neighbour is outside the grid, skip
            if k < 0 or k >= self.n or l == self.m:
                continue
            
            # If the neighbour is smaller or equal to current cell, skip
            if self.grid[i][j] >= self.grid[k][l]:
                continue

            # Compute the number of moves from this neighbour
            max_moves = max(1 + self.opt(k, l), max_moves)
        
        # Return the maximum number of moves from this cell
        return max_moves



# opt(i, j) - The maximum number of moves that can be done
#             starting from the cell (i, j)

# Base case:
# opt(i, j) = 0         if (i, j) is a local maxima

# Recurrency:
# opt(i, j) = 1 + max(opt(i', j') 
#                     for (i', j') in neighbourhood
#                     if grid[i][j] < grid[i'][j'])