# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(mn)

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        # Using BFS
        m, n = len(grid), len(grid[0])

        # Iterate the grid
        seen = set()
        for i in range(m):
            for j in range(n):
                # If we are at an unseen cell, perform BFS
                if (i, j) in seen:
                    continue
                
                queue = deque([((i, j), None)])
                while queue:
                    position, last = queue.popleft()
                    
                    # If we ever find a seen neighbour, we have a cycle
                    if position in seen:
                        return True
                    seen.add(position)
                    
                    # Otherwise, add all neighbour cells of the same value to queue
                    for a, b in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        new_position = (position[0] + a, position[1] + b)
                        if new_position[0] < 0 or new_position[0] >= m or new_position[1] < 0 or new_position[1] >= n:
                            continue
                        
                        if new_position != last and grid[new_position[0]][new_position[1]] == grid[i][j]:
                            queue.append(((position[0] + a, position[1] + b), position))
        
        # If the loop terminates, there does not exist any same-valued cycles
        return False
