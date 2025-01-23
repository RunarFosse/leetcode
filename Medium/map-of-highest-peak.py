# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(mn)

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        # Using BFS
        m, n = len(isWater), len(isWater[0])
        
        # Add all water cells to the queue
        queue = deque([])
        for i in range(m):
            for j in range(n):
                if isWater[i][j]:
                    queue.append((i, j, 0))
                isWater[i][j] = None
        
        # Then perform BFS
        while queue:
            i, j, distance = queue.popleft()
            if isWater[i][j] is not None:
                continue

            # Override isWater grid to store peak height
            isWater[i][j] = distance

            # Add all neighbours to queue
            for a, b in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if 0 <= i + a < m and 0 <= j + b < n:
                    queue.append((i + a, j + b, distance + 1))
        
        # Finally, return map over area with maximized peaks
        return isWater
