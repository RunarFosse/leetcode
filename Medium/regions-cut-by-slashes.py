# Author: Runar Fosse
# Time complexity: O(n^2)
# Space complexity: O(n^2)

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        # Using BFS
        n = len(grid)

        # Create an image of the grid subdivided into nine
        image = [[0] * 3*n for _ in range(3*n)]
        for i, j in product(range(n), range(n)):
            if grid[i][j] == "\\":
                image[3*i][3*j] = None
                image[3*i+1][3*j+1] = None
                image[3*i+2][3*j+2] = None
            elif grid[i][j] == "/":
                image[3*i][3*j+2] = None
                image[3*i+1][3*j+1] = None
                image[3*i+2][3*j] = None
        
        # Then iterate the image, counting the number of separated regions
        regions = 0
        for i, j in product(range(3*n), range(3*n)):
            if image[i][j] == None or image[i][j] > 0:
                continue
            
            # If image cell is 0, we've hit a new region
            regions += 1

            # Thus perform BFS from this image cell
            queue = deque([(i, j)])
            while queue:
                y, x = queue.popleft()
                if image[y][x] == None or image[y][x] > 0:
                    continue

                # Mark current position as visited
                image[y][x] = regions 

                # Add neighbouring cells to queue and continue
                if y > 0:
                    queue.append((y-1, x))
                if y < 3*n-1:
                    queue.append((y+1, x))
                if x > 0:
                    queue.append((y, x-1))
                if x < 3*n-1:
                    queue.append((y, x+1))
        
        print(image)

        # Return the number of separate regions
        return regions

# If we subdivide the input grid into nine, we can accurately 
# represent regions cut by diagonal slashes.