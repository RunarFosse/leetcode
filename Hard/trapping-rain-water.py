# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def trap(self, heights: List[int]) -> int:
        # Divide list into 2 parts
        # (Approachable from left, and approachable from right)
        split = len(heights)
        max_height = 0
        for i in range(split-1, -1, -1):
            if heights[i] > max_height:
                max_height = heights[i]
                split = i

        # Approach from left
        height = 0
        total_water = 0
        for i in range(split):
            if heights[i] > height:
                height = heights[i]
            else:
                total_water += height - heights[i]
        
        # Approach from right
        height = 0
        for i in range(len(heights)-1, split, -1):
            if heights[i] > height:
                height = heights[i]
            else:
                total_water += height - heights[i]
        
        return total_water