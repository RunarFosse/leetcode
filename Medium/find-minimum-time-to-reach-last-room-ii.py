# Author: Runar Fosse
# Time complexity: O(mnlog(mn))
# Space complexity: O(mn)

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        # Using Dijkstra's
        n, m = len(moveTime), len(moveTime[0])

        # Iterate the grid greedily by time
        queue, seen = [(0, (0, 0), 1)], set()
        while queue:
            time, (i, j), speed = heappop(queue)
            if (i, j) in seen:
                continue
            seen.add((i, j))

            # If we've reached the end, return
            if (i, j) == (n - 1, m - 1):
                return time

            # Add all neighbour cells at their respective times
            for a, b in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if i + a < 0 or i + a >= n or j + b < 0 or j + b >= m:
                    continue
                timeToMove = max(time, moveTime[i + a][j + b]) + speed
                heappush(queue, (timeToMove, (i + a, j + b), speed % 2 + 1))