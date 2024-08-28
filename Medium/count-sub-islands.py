# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(mn)

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        # Using BFS
        m, n = len(grid1), len(grid1[0])

        # Iterate over each cell in the second grid
        sub_islands = 0
        for i in range(m):
            for j in range(n):
                if not grid2[i][j]:
                    continue
                
                # If we find an island
                is_sub = True

                # Mark cell as visited
                grid2[i][j] = 0

                # Breadth-first search the full island
                queue = deque([(i, j)])
                while queue:
                    y, x = queue.popleft()

                    # If any grid cell is not an island in grid1,
                    # the current island is not a sub island
                    if not grid1[y][x]:
                        is_sub = False
                    
                    # Add neighbour island cells to queue
                    for a, b in [(y+1, x), (y-1, x), (y, x+1), (y, x-1)]:
                        if a < 0 or a >= m or b < 0 or b >= n or not grid2[a][b]:
                            continue
                        grid2[a][b] = 0
                        queue.append((a, b))
                
                # If island is a sub island, count it
                if is_sub:
                    sub_islands += 1
        
        # Return the number of sub islands
        return sub_islands