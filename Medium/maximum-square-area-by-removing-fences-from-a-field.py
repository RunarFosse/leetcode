# Author: Runar Fosse
# Time complexity: O(h^2 + v^2)
# Space complexity: O(h^2)

class Solution:
    mod = int(1e9 + 7)
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        # Append boundary fences to each of the arrays
        hFences.extend([1, m])
        vFences.extend([1, n])
        h, v = len(hFences), len(vFences)

        # First, compute possible square widths by removing fences
        widths = set()
        for i in range(h):
            for j in range(i + 1, h):
                width = abs(hFences[i] - hFences[j])
                widths.add(width)
        
        # Then, compute possible square heights by removing fences
        maximum = 0
        for i in range(v):
            for j in range(i + 1, v):
                height = abs(vFences[i] - vFences[j])

                # If this height was seen as a width, store the maximum
                if height in widths:
                    maximum = max(height, maximum)
        
        # Then finally, return the largest possible area of the square
        if not maximum:
            return -1
        return maximum * maximum % self.mod
