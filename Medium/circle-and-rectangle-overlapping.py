# Author: Runar Fosse
# Time complexity: O(1)
# Space complexity: O(1)

class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        # Find the closest point of the circle lying on the rectangle border
        closest = (max(x1, min(xCenter, x2)), max(y1, min(yCenter, y2)))

        # Compute the squared distance between this point and the circle center
        difference = (xCenter - closest[0], yCenter - closest[1])
        distance = difference[0] * difference[0] + difference[1] * difference[1]

        # If this distance is smaller than the radius squared, they overlap
        return distance <= radius * radius
