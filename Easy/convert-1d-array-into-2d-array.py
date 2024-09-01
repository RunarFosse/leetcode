# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(mn)

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        # If original does not match size of 2D array, return empty list
        if m * n != len(original):
            return []

        # If not, reshape into 2D
        return [original[i * n:(i+1) * n] for i in range(m)]