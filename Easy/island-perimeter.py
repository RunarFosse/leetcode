# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(mn)

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # Using BFS
        m, n = len(grid), len(grid[0])

        # First find a piece of land
        start = None
        for y in range(m):
            if not start:
                for x in range(n):
                    if grid[y][x]:
                        start = (y, x)
                        break
        
        # Then Breadth-first search from that piece of land,
        # counting perimeter
        perimeter = 0
        queue, seen = [start], set()
        while queue:
            y, x = queue.pop()
            if (y, x) in seen:
                continue
            
            seen.add((y, x))
            # Count and add all neighbouring island cells
            neighbours = []
            if y > 0 and grid[y-1][x]:
                neighbours.append((y-1, x))
            if y < m-1 and grid[y+1][x]:
                neighbours.append((y+1, x))
            if x > 0 and grid[y][x-1]:
                neighbours.append((y, x-1))
            if x < n-1 and grid[y][x+1]:
                neighbours.append((y, x+1))
            
            # Add perimeters
            perimeter += 4 - len(neighbours)

            # And add non-seen to queue
            queue += [cell for cell in neighbours if cell not in seen]
        
        return perimeter