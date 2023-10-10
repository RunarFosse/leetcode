# Author: Runar Fosse
# Time complexity: O(log(n*m))
# Space complexity: O(1)

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Using binary search
        n, m = len(matrix[0]), len(matrix)
        left, right = 0, n*m
        while left < right:
            pivot = (left + right) // 2
            row, col = divmod(pivot, n)

            if matrix[row][col] == target:
                return True

            if left == right - 1:
                break

            if matrix[row][col] < target:
                left = pivot
            else:
                right = pivot
        
        return False