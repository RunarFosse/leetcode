# Author: Runar Fosse
# Time complexity: O(m^2 + n^2)
# Space complexity: O(mn)

class Solution:
    # Store direction order in a dictionary
    nextDirection = {(0, 1): (1, 0),
                     (1, 0): (0, -1),
                    (0, -1): (-1, 0),
                    (-1, 0): (0, 1)}

    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        visited = [[rStart, cStart]]
        
        # Denote the starting direction to walk and stride size
        stride, direction = 1, (0, 1)
        while len(visited) < rows * cols:
            # Walk until stride is reached
            for _ in range(stride):
                rStart += direction[0]
                cStart += direction[1]

                # If position is inside matrix, add to list
                rValid = rStart >= 0 and rStart < rows
                cValid = cStart >= 0 and cStart < cols
                if rValid and cValid:
                    visited.append([rStart, cStart])
            
            # Update direction and increment stride if needed
            stride += abs(direction[0])
            direction = self.nextDirection[direction]
        
        # Return all visited matrix cells
        return visited
