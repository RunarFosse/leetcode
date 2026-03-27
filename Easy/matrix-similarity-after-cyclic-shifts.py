# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(1)

class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        # Using simulation
        m, n = len(mat), len(mat[0])

        # If k is a multiple of n
        if not k % n:
            # Then the matrix will remain unchanged
            return True

        # Otherwise, iterate each row
        for i in range(m):
            # Simulate shifts
            for j in range(n):
                # By computing the new element after shifting
                new_j = (j - k if i % 2 else j + k) % n

                # If the current and new element are not equal
                if mat[i][j] != mat[i][new_j]:
                    # Then shifted matrix will not be identical to the current
                    return False
        
        # However if the loop terminates, then the shifted matrix is identical
        return True
