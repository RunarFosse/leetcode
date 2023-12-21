# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        # Using greedy
        points.sort()

        # Iterate points array, storing maximum x-difference between to consecutive points
        return max(points[i][0] - points[i-1][0] for i in range(1, len(points)))

# Merge sort has time complexity of O(nlog n) and space complexity of O(n).
# This is our bottleneck.