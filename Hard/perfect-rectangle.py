# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        # Check if sum of all rectangles equal sum of bounding rectangle
        bottomleft, topright = (1e9, 1e9), (-1e9, -1e9)
        sumarea = 0
        corners = {}
        for x, y, a, b in rectangles:
            sumarea += (a-x)*(b-y)
            bottomleft = (min(x, bottomleft[0]), min(y, bottomleft[1]))
            topright = (max(a, topright[0]), max(b, topright[1]))

            # Increment count of all 4 corners
            if (x,y) not in corners:
                corners[(x,y)] = 0
            corners[(x,y)] += 1
            if (a,b) not in corners:
                corners[(a,b)] = 0
            corners[(a,b)] += 1
            if (x,b) not in corners:
                corners[(x,b)] = 0
            corners[(x,b)] += 1
            if (a,y) not in corners:
                corners[(a,y)] = 0
            corners[(a,y)] += 1
        
        # A rectangle is non-overlapping if outer corners only appear once
        # and inner corners either occur twice or four times
        for corner, count in corners.items():
            if (corner in [bottomleft, topright, (bottomleft[0], topright[1]), (topright[0], bottomleft[1])]):
                if count == 1:
                    continue
                return False
            if count % 2:
                return False

        # If it is, then do the sum check
        return sumarea == (topright[0]-bottomleft[0])*(topright[1]-bottomleft[1])