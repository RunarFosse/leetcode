# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(1)

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        # Using convolution
        m, n = len(grid), len(grid[0])
    
        # Iterate over each grid cell
        magics = 0
        for i in range(m-2):
            for j in range(n-2):
                # Loop over the square, verifying all requirements
                distincts, numbers = True, [0] * 9
                rows, cols, diags = [0] * 3, [0] * 3, [0] * 2
                for a, b in product(range(3), range(3)):
                    num = grid[i+a][j+b]

                    # Verify that number is between 1 and 9, and distinct
                    if not num or num > 9 or numbers[num-1]:
                        distincts = False
                        break
                    numbers[num-1] += 1

                    # Calculate row, column and diagonal sums
                    rows[a] += num
                    cols[b] += num
                    if a == b:
                        diags[0] += num
                    if a == 2-b:
                        diags[1] += num
                    
                # If distinct requirement is not met, continue outer loop
                if not distincts:
                    continue

                # Then if all the sums are equal, this is a magic square
                rows_valid = rows[0] == rows[1] and rows[1] == rows[2]
                cols_valid = cols[0] == cols[1] and cols[1] == cols[2]
                diags_valid = diags[0] == diags[1]
                all_valid = rows[0] == cols[0] and cols[0] == diags[0]
                if rows_valid and cols_valid and diags_valid and all_valid:
                    magics += 1

        # Return the number of magic squares
        return magics