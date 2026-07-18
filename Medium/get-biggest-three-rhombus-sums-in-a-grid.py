# Author: Runar Fosse
# Time complexity: O(mn * min(m, n))
# Space complexity: O(mn)

class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        # Using prefix sum
        m, n = len(grid), len(grid[0])

        # First, compute the diagonal prefix sums (main and anti-diagonal)
        mains = [[0] * (n + 2) for _ in range(m + 1)]
        antis = [[0] * (n + 2) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                mains[i][j] = mains[i - 1][j - 1] + grid[i - 1][j - 1]
                antis[i][j] = antis[i - 1][j + 1] + grid[i - 1][j - 1]

        # Then, iterate every cell
        rhombi = []
        for i in range(m):
            for j in range(n):
                # Iterate every possible rhombus
                maximum = (min(m - i, n - j) + 1) // 2
                for size in range(maximum):
                    border = grid[i][j]

                    # If rhombus is not trivial
                    if size > 0:
                        # Compute its corners
                        top, bottom = (i, j + size), (i + 2 * size, j + size)
                        left, right = (i + size, j), (i + size, j + 2 * size)

                        # And, using prefix sums, compute border value
                        border = (
                            mains[right[0] + 1][right[1] + 1] - mains[top[0]][top[1]]
                            + mains[bottom[0] + 1][bottom[1] + 1] - mains[left[0]][left[1]]
                            + antis[left[0] + 1][left[1] + 1] - antis[top[0]][top[1] + 2]
                            + antis[bottom[0] + 1][bottom[1] + 1] - antis[right[0]][right[1] + 2]
                            - grid[right[0]][right[1]]
                            - grid[top[0]][top[1]]
                            - grid[bottom[0]][bottom[1]]
                            - grid[left[0]][left[1]]
                        )
                    
                    # Storing the three largest distinct rhombi
                    self.storeDistinctKLargestSorted(border, rhombi, 3)
        
        # Finally, return the three largest rhombi
        return rhombi
    
    def storeDistinctKLargestSorted(self, value: int, values: List[int], k: int) -> None:
        # Get the intended index of this value
        index = bisect_left(values, -value, key=lambda e: -e)

        # If this value is already in the list, do not add another
        if index < len(values) and values[index] == value:
            return
        
        # If the intended index is within the k largest
        if index < k:
            # Insert it
            values.insert(index, value)
        
        # And remove last element if exceeding size k
        if len(values) > k:
            values.pop()
