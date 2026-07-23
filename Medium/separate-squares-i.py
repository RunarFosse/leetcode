# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        # First, iterate all the squares
        area, horizontals = 0, []
        for x, y, length in squares:
            # Compute total square covered area
            area += length * length

            # And gather all square horizontal edges
            horizontals.append((y, length, True))
            horizontals.append((y + length, length, False))
        
        # Then, sort these horizontal edges in ascending order based on y-coordinate
        horizontals.sort()

        # While scanning over each, keep track of area under line and current total width
        current_area, current_width = 0, 0

        # Then, scan a horizontal line over all the squares
        y_last = 0
        for y, length, starts in horizontals:
            # Get the last height difference
            difference = y - y_last

            # And update the current square area under scanline
            current_area += difference * current_width

            # If the area below now exceeds half the total area
            if 2 * current_area >= area:
                # Compute by how much
                excess = 2 * current_area - area

                # Divide it by the width and average to find height reduction for split
                reduction = excess / (current_width * 2)

                # And use this reduction to return the minimum splitting y-coordinate
                return y - reduction

            # Otherwise, based on if new edge ends or starts a new square, add to width
            current_width += length if starts else -length

            # And update this as the last seen y-coordinate
            y_last = y
