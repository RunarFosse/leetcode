# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0
        for i in range(0, len(points) - 1):
            start, end = points[i], points[i+1]
            time += max(abs(end[0] - start[0]), abs(end[1] - start[1]))
        return time