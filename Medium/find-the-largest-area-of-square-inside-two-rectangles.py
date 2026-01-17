# Author: Runar Fosse
# Time complexity: O(n^2)
# Space complexity: O(1)

class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        # Using geometry
        n = len(bottomLeft)

        # Iterate every pair of squares
        maximum = 0
        for i in range(n):
            for j in range(i + 1, n):
                (xmin1, ymin1), (xmax1, ymax1) = bottomLeft[i], topRight[i]
                (xmin2, ymin2), (xmax2, ymax2) = bottomLeft[j], topRight[j]

                # Compute the corners of their intersecting rectangle
                xmin, ymin = max(xmin1, xmin2), max(ymin1, ymin2)
                xmax, ymax = min(xmax1, xmax2), min(ymax1, ymax2)

                # And if they intersect
                if xmin < xmax and ymin < ymax:
                    # Store the maximum area of a square that can fit inside
                    side = min(xmax - xmin, ymax - ymin)
                    maximum = max(side * side, maximum)
    
        # Finally, return the area of the largest intersection
        return maximum
