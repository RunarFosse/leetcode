# Author: Runar Fosse
# Time complexity: O(n^2log n)
# Space complexity: O(n^2)

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        # Using Dijkstra's
        n = len(grid)

        # First, iterate the grid
        queue = deque([])
        for i in range(n):
            for j in range(n):
                # Adding the every thief to the queue
                if grid[i][j]:
                    queue.append((i, j, 0))
        
        # Then, perform BFS from every thief
        safenesses = [[None] * n for _ in range(n)]
        while queue:
            i, j, safeness = queue.popleft()
            if safenesses[i][j] is not None:
                continue

            # Computing the safeness factor of each cell
            safenesses[i][j] = safeness

            for a, b in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if 0 <= i + a < n and 0 <= j + b < n:
                    queue.append((i + a, j + b, safeness + 1))
        
        # Now, find the safest queue from top-left to bottom-right using Dijkstra's
        queue, seen = [(-n, 0, 0)], set()
        while queue:
            minimum, i, j = heappop(queue)
            if (i, j) in seen:
                continue
            seen.add((i, j))

            # Store the negated minimum safeness of this path
            minimum = max(-safenesses[i][j], minimum)

            # If at the end, this minimum safeness factor denotes maximum path safeness
            if (i, j) == (n - 1, n - 1):
                return -minimum

            for a, b in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if 0 <= i + a < n and 0 <= j + b < n:
                    heappush(queue, (minimum, i + a, j + b))
