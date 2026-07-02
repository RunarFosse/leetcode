# Author: Runar Fosse
# Time complexity: O(mnlog(mn))
# Space complexity: O(mn)

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        # Using min heap
        m, n = len(heightMap), len(heightMap[0])

        # First, add all edge cells to the min heap queue
        queue, visited = [], [[False] * n for _ in range(m)]
        for i in range(m):
            for j in [0, n - 1]: 
                queue.append((heightMap[i][j], i, j))
                visited[i][j] = True
        for j in range(1, n - 1):
            for i in [0, m - 1]: 
                queue.append((heightMap[i][j], i, j))
                visited[i][j] = True
        heapify(queue)
        
        # Then, expand inwards from the edge
        total_water = 0
        while queue:
            height, i, j = heappop(queue)

            # Iterate the neighbours
            for a, b in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if not (0 <= i + a < m and 0 <= j + b < n) or visited[i + a][j + b]:
                    continue
                
                # Compute its minimum water height capacity based on our height
                capacity = max(height, heightMap[i + a][j + b])

                # Update total trapped water
                total_water += capacity - heightMap[i + a][j + b]

                # And add neighbour to queue with its new capacity as height
                heappush(queue, (capacity, i + a, j + b))
                visited[i + a][j + b] = True
        
        # Finally, return the total amount of water trapped
        return total_water
