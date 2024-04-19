# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(mn)

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Using BFS
        m, n = len(grid), len(grid[0])
        visited = set()
        islands = 0

        # First find all unvisited islands
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0" or (i, j) in visited:
                    continue
                
                islands += 1
                queue = deque([(i, j)])
                while queue:
                    y, x = queue.popleft()
                    if (y, x) in visited:
                        continue
                    visited.add((y, x))
                    
                    # Add all unvisited neighbours to queue
                    if y > 0 and grid[y-1][x] == "1":
                        if (y-1, x) not in visited:
                            queue.append((y-1, x))
                    if y < m-1 and grid[y+1][x] == "1":
                        if (y+1, x) not in visited:
                            queue.append((y+1, x))
                    if x > 0 and grid[y][x-1] == "1":
                        if (y, x-1) not in visited:
                            queue.append((y, x-1))
                    if x < n-1 and grid[y][x+1] == "1":
                        if (y, x+1) not in visited:
                            queue.append((y, x+1))
                         
        # Return the number of islands
        return islands