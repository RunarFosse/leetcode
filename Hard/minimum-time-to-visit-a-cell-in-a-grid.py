# Author: Runar Fosse
# Time complexity: O(mnlog(mn))
# Space complexity: O(mn)

class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        # Using Dijkstra's
        m, n = len(grid), len(grid[0])

        # Firstly, check that we actually can walk from start position
        if grid[1][0] > 1 and grid[0][1] > 1:
            return -1

        queue, seen = [(0, (0, 0))], set()
        while queue:
            time, (i, j) = heappop(queue)
            if (i, j) in seen:
                continue
            seen.add((i, j))

            # If this is the bottom-right corner, return time
            if (i, j) == (m - 1, n - 1):
                return time
            
            # Add all neighbours we can move to, to queue
            for a, b in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if i+a < 0 or i+a >= m or j+b < 0 or j+b >= n:
                    continue
                
                # If we can go there instantly, do so
                if grid[i+a][j+b] <= time + 1:
                    heappush(queue, (time + 1, (i+a, j+b)))
                    continue

                # If not, compute the wait time by spinning back and forth
                wait = grid[i+a][j+b] - time
                if grid[i+a][j+b] % 2 != time % 2:
                    wait -= 1
                heappush(queue, (time + wait + 1, (i+a, j+b)))