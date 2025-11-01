# Author: Runar Fosse
# Time complexity: O(n^3)
# Space complexity: O(1)

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        # Iterate over every triple of points
        maximum = 0
        for (x1, y1), (x2, y2), (x3, y3) in combinations(points, 3):
            # Compute the area of the given triangle using the determinant
            area = 0.5 * abs(x1 * (y2 - y3) - x2 * (y1 - y3) + x3 * (y1 - y2))

            # And store the maximum area
            maximum = max(area, maximum)
        
        # Finally, return said maximum area
        return maximum
