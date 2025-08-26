# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        # Iterate all the rectangles
        area, diagonal = 0, 0
        for length, width in dimensions:
            # If the current rectangle has the longest diagonal (squared)
            current = pow(length, 2) + pow(width, 2)
            if current > diagonal:
                # Store it, and the current area
                diagonal = current
                area = length * width

            # If it is equal to the diagonal
            elif current == diagonal:
                # Store the maximum area
                area = max(length * width, area)
        
        # Finally, return the area of the rectangle with the longest diagonal
        return area
        