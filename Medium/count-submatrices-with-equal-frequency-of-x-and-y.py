# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(n)

class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        # Using prefix sum
        m, n = len(grid), len(grid[0])

        # Compute the column prefix sum of the grid
        count, columns = 0, [(0, False)] * n
        for i in range(m):
            # For each row, compute the current X/Y balance
            current = (0, False)
            for j in range(n):
                # Get the current character
                char = grid[i][j]

                # If the character is X, increment prefix, else if Y, decrement
                prefix, contains = columns[j]
                if char == "X":
                    # If we've seen an X, stored it as 'contains'
                    contains = True
                    prefix += 1
                elif char == "Y":
                    prefix -= 1
                
                # Update the prefix sum
                columns[j] = (prefix, contains)

                # Also count it towards current count
                current = (current[0] + prefix, current[1] or contains)

                # If we have an equal balance, and submatrix contains an X, count it
                if not current[0] and current[1]:
                    count += 1
        
        # Finally, return the number of valid submatrices
        return count
