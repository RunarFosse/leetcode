# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(mn)

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        # Using BFS
        m, n = len(grid), len(grid[0])

        queue, seen = deque([((0, 0), 0)]), set()
        while queue:
            # Pop a position from the queue
            (i, j), obstacles = queue.popleft()
            if (i, j) in seen:
                continue
            seen.add((i, j))

            # If we've reached the end, return
            if i == m - 1 and j == n - 1:
                return obstacles
            
            # Add all neighbours to the queue
            for a, b in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if i+a < 0 or i+a >= m or j+b < 0 or j+b >= n:
                    continue
                
                # If the neighbour has an obstacle, add it to the end
                if grid[i+a][j+b]:
                    queue.append(((i+a, j+b), obstacles + 1))

                # If not, add it to the front for prioritized exploration!
                else:
                    queue.appendleft(((i+a, j+b), obstacles))

# By adding empty positions to the front of the deque, we can explore 
# all empty routes first, guaranteeing we find the fastest route with least
# obstacles in an efficient way!