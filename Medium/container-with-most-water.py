# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # This question is poorly formulated
        # Solved using two pointer approach

        start, end = 0, len(height) - 1
        maxarea = 0
        while start != end:
            area = (end - start) * min(height[start], height[end])
            maxarea = max(area, maxarea)

            if height[start] < height[end]:
                start += 1
            else:
                end -= 1

        return maxarea
