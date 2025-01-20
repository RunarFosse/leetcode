# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(mn)

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        # Using BFS
        m, n = len(grid), len(grid[0])
        
        # First turn the grid into a graph
        adjls = defaultdict(list)
        for i in range(m):
            for j in range(n):
                # Add all valid neighbours
                for k, (a, b) in enumerate([(0, 1), (0, -1), (1 ,0), (-1, 0)]):
                    if i + a < 0 or i + a >= m or j + b < 0 or j + b >= n:
                        continue

                    # If the gridcell is not ponting to neighbour, add weight
                    weight = 0 if grid[i][j] == k + 1 else 1
                    adjls[(i, j)].append(((i + a, j + b), weight))

        # Then perform BFS starting at the upper left corner
        queue, seen = deque([((0, 0), 0)]), set()
        while queue:
            position, distance = queue.popleft()
            if position in seen:
                continue
            seen.add(position)

            # If we reach the end, return the current distance
            if position == (m - 1, n - 1):
                return distance

            # If not, add all current neighbours into queue
            for neighbour, weight in adjls[position]:
                # If weight is zero, add to start in queue, if not add to end
                if not weight:
                    queue.appendleft((neighbour, distance))
                else:
                    queue.append((neighbour, distance + weight))
                    