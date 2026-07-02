# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(mn)

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        # Using BFS
        m, n = len(grid), len(grid[0])

        # Perform 0-1 BFS on the grid
        queue, seen = deque([(0, 0, health)]), set()
        while queue:
            i, j, health = queue.popleft()

            # Decrement health if we are on an unsafe cell
            health -= grid[i][j]

            # If we are dead, or we've been here before, skip
            if not health or (i, j) in seen:
                continue
            seen.add((i, j))

            # Return if we've reached the end
            if (i, j) == (m - 1, n - 1):
                return True
            
            # Then add all neighbours to the queue
            for a, b in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if 0 <= i + a < m and 0 <= j + b < n:
                    # If next grid is safe, add to beginning of queue, otherwise to end
                    neighbour = (i + a, j + b, health)
                    if grid[i + a][j + b]:
                        queue.append(neighbour)
                    else:
                        queue.appendleft(neighbour)
        
        # If loop terminates, we cannot get to the end safely
        return False
