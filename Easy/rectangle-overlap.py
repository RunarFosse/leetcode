# Author: Runar Fosse
# Time complexity: O(1)
# Space complexity: O(1)

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # First, unpack each rectangle
        x11, y11, x12, y12 = rec1
        x21, y21, x22, y22 = rec2
            
        # Compute predicates to check whether the rectangles collide
        is_left = x11 < x22
        is_right = x12 > x21
        is_above = y11 < y22
        is_below = y12 > y21

        # If all predicates are true, they collide
        return is_left and is_right and is_above and is_below
