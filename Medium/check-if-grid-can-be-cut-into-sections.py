# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        # Sort rectangles by order of ascending horizontal position
        rectangles.sort(key=lambda r: (r[0], r[2]))

        # Then merge all horizontally overlapping rectangles
        cut, horizontals = 1, 0
        for start, _, end, _ in rectangles:
            if start >= cut:
                horizontals += 1
            cut = max(end, cut) 

        # Then sort by order of ascending vertical position
        rectangles.sort(key=lambda r: (r[1], r[3]))

        # Then merge all vertically overlapping rectangles
        cut, verticals = 1, 0
        for _, start, _, end in rectangles:
            if start >= cut:
                verticals += 1
            cut = max(end, cut) 

        # Check if we can make at least two horizontal or vertical cuts
        return horizontals >= 2 or verticals >= 2