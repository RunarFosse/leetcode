# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(mn)

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # Using dynamic programming
        self.obstacleGrid = obstacleGrid
        self.m, self.n = len(obstacleGrid) - 1, len(obstacleGrid[0]) - 1

        # There could be an obstacle under robot (??) or under star (???), return 0 if so
        if obstacleGrid[0][0] or obstacleGrid[self.m][self.n]:
            return 0

        return self.uniquePaths(0, 0)
        
    @functools.cache
    def uniquePaths(self, y: int, x: int) -> int:
        # Check that straight path down or right is clear
        if y == self.m:
            while x < self.n:
                if self.obstacleGrid[y][x]:
                    return 0
                x += 1
            return 1
        if x == self.n: 
            while y < self.m:
                if self.obstacleGrid[y][x]:
                    return 0
                y += 1
            return 1
        
        # Add paths from unoccupied position 
        paths = 0
        if not self.obstacleGrid[y+1][x]:
            paths += self.uniquePaths(y+1, x)
        if not self.obstacleGrid[y][x+1]:
            paths += self.uniquePaths(y, x+1)
        return paths


# opt(x, y) - Optimal solution starting at top left (0, 0) corner of (m, n) rectangle

# Base case:
# opt(m, x) = 1 if the path is without obstacles else 0
# opt(y, n) = 1 if the path is without obstacles else 0

# Recurrency:
# opt(y, x) = opt(y+1, x) if not obstacleGrid[y+1, x] else 0
#           + opt(y, x+1) if not obstacleGrid[y, x+1] else 0

# Number of states = m*n, runtime per state = O(1)