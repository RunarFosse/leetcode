# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(mn)

class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        # Create a grid with a free path along the top and right side
        grid = [("." * n) if i == 0 else ("#" * (n - 1) + ".") for i in range(m)]
        return grid
