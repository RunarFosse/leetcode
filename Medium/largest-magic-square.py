# Author: Runar Fosse
# Time complexity: O(mn * min(m, n)^2)
# Space complexity: O(mn)

class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        # Using prefix sum
        m, n = len(grid), len(grid[0])

        # Compute prefix sum of row, column and diagonals
        rows, columns = [[0] for _ in range(m)], [[0] for _ in range(n)]
        major_diagonals, minor_diagonals = ([[0] for _ in range(m + n)], [[0] for _ in range(m + n)])
        for i in range(m):
            for j in range(n):
                value = grid[i][j]
                rows[i].append(value + rows[i][-1])
                columns[j].append(value + columns[j][-1])

                # Compute the diagonal index as combination of row and column
                major, minor = n - (j + 1) + i, i + j
                major_diagonals[major].append(value + major_diagonals[major][-1])
                minor_diagonals[minor].append(value + minor_diagonals[minor][-1])

        # Then, iterate every possible subsquare of the matrix
        maximum = 0
        for i in range(m):
            for j in range(n):
                for k in reversed(range(1, min(m - i, n - j) + 1)):
                    # Verify that the subsquare is a magic square
                    target = rows[i][j + k] - rows[i][j]

                    # Creating a helper function to simplify computation
                    def isValid(index: int) -> Callable[[list], bool]:
                        return lambda list: list[index + k] - list[index] == target

                    # First check if diagonals match
                    major, minor = n - (j + 1) + i, i + j + (k - 1)
                    major_diagonal, minor_diagonal = major_diagonals[major], minor_diagonals[minor]
                    diagonals_valid = isValid(min(i, j))(major_diagonal) and isValid(min(i, n - (j + k)))(minor_diagonal)

                    # If they don't, skip out early
                    if not diagonals_valid:
                        continue

                    # Otherwise, check if rows and columns are valid
                    row_valid = all(map(isValid(j), rows[i:i+k]))
                    column_valid = all(map(isValid(i), columns[j:j+k]))

                    # If they are, we have a magic square
                    if row_valid and column_valid:
                        # Store the maximum magic square size in the matrix
                        maximum = max(k, maximum)

                        # And break out early, as no larger square can be found here
                        break

        # Finally, return the size of the largest magic square in the grid
        return maximum
