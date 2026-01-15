# Author: Runar Fosse
# Time complexity: O(hlog h + vlog v)
# Space complexity: O(h + v)

class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        # Using sorting
        h, v = len(hBars), len(vBars)
        
        # First, sort all bars in ascending order
        hBars.sort()
        vBars.sort()

        # Then, iterate all bars, storing longest sequence of bars differing by one
        current, horizontal = 0, 0
        for i in range(h):
            if i and hBars[i] != hBars[i - 1] + 1:
                current = 0
            current += 1
            horizontal = max(current, horizontal)
        current, vertical = 0, 0
        for i in range(v):
            if i and vBars[i] != vBars[i - 1] + 1:
                current = 0
            current += 1
            vertical = max(current, vertical)
        
        # Then, compute and return the largest possible hole by removing bars
        side = min(horizontal, vertical) + 1
        return side * side
