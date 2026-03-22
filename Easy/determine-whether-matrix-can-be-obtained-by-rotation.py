# Author: Runar Fosse
# Time complexity: O(n^2)
# Space complexity: O(1)

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        # Using matrix rotations
        n = len(mat)
        
        # If the two matrices are equal initially, return early
        if mat == target:
            return True
        
        # Otherwise, perform 3, 90 degree clockwise rotations of mat
        for _ in range(3):
            # First, transpose the matrix
            for i in range(n):
                for j in range(i + 1, n):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
            
            # Then, reverse each row
            for i in range(n):
                mat[i].reverse()
            
            # Then check if they are equal
            if mat == target:
                return True
        
        # If all rotations are made, target cannot be obtained through rotations
        return False
