# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(m + n)

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        # Using BFS
        m, n = len(grid), len(grid[0])

        # Store maximum number of fish
        max_fish = 0

        # Iterate every grid cell
        for r in range(m):
            for c in range(n):
                # BFS and count number of fish
                fish, queue = 0, deque([(r, c)])
                while queue:
                    i, j = queue.popleft()

                    # If there are no fish, skip
                    if not grid[i][j]:
                        continue

                    # Otherwise, count and set to zero
                    fish += grid[i][j]
                    grid[i][j] = 0
                    
                    # Add neighbour cells
                    for a, b in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        if i + a < 0 or i + a >= m or j + b < 0 or j + b >= n:
                            continue
                        
                        queue.append((i + a, j + b))
                
                # Update max fish count
                max_fish = max(fish, max_fish)
        
        # Finally, return the maximum number of catchable fish
        return max_fish