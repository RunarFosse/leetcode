# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # Using Dijkstra's algorithm
        m, n = len(grid) - 1, len(grid[0]) - 1
        
        # Turn queue into priority_queue
        queue = [(grid[0][0], (0,0))]
        visited = set((0, 0))
        heapq.heapify(queue)
        while queue:
            distance, position = heapq.heappop(queue)

            # Return if we are at target
            if position == (m, n):
                return distance

            # Add down if can go down and not previously visited
            if position[0] < m:
                next_position = (position[0] + 1, position[1])
                if next_position not in visited:
                    visited.add(next_position)
                    next_distance = distance + grid[next_position[0]][next_position[1]]
                    heapq.heappush(queue, (next_distance, next_position))
            # Add right if can go right and not previously visited
            if position[1] < n: 
                next_position = (position[0], position[1] + 1)
                if next_position not in visited:
                    visited.add(next_position)
                    next_distance = distance + grid[next_position[0]][next_position[1]]
                    heapq.heappush(queue, (next_distance, next_position))