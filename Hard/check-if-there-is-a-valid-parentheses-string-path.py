# Author: Runar Fosse
# Time complexity: O(mn(m + n))
# Space complexity: O(n(m + n))

class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        # Using dynamic programming
        m, n = len(grid), len(grid[0])

        # Iterate every row
        diagonal = max(m, n)
        opt = [[False for _ in range(diagonal)] for _ in range(n)]
        for i in reversed(range(m)):
            # Create a temporary version of the state array
            temp = [[False for _ in range(diagonal)] for _ in range(n)]

            # Then, iterate every column
            for j in reversed(range(n)):
                # Check if the current cell opens or closes a parenthesis pair
                change = 1 if grid[i][j] == "(" else -1

                # And every possible open parentheses count
                possible = min(diagonal, m - i + n - j)
                for count in range(possible):
                    # Skip invalid solutions
                    if count + change < 0 or count + change == diagonal:
                        continue
                    
                    # If we are at the end cell
                    if i == m - 1 and j == n - 1:
                        # Then we have a valid parentheses string path if total count is 0
                        temp[j][count] = (count + change) == 0
                        continue

                    # If we can, test going down
                    if i < m - 1:
                        temp[j][count] |= opt[j][count + change]
                    # Or going right
                    if j < n - 1:
                        temp[j][count] |= temp[j + 1][count + change]
                
            # At last, override the current dynamic programming state array
            opt = temp
                    
        # Finally, return if we can construct a valid parentheses string path from start
        return opt[0][0]


# By counting #open_paranthesis - #closed_paranthesis we can easily check whether a
# current string path is valid, by strictly only accepting non-negative solutions,
# that result in a count of 0. This means they result in a valid parentheses string.

# opt(i, j, k) - If there exists a valid parentheses string path starting in cell (i, j)
#                given that the current paranthesis path count is equal to k.

# Base case:
# opt(i, j, k < 0 or k > m - i + n - j) = False
# opt(m, _, _) = False
# opt(_, n, _) = False
# opt(m - 1, n - 1, k) = True if k == 1 and grid[m - 1][n - 1] == ")" else False

# Recurrency:
# opt(i, j, k) | grid[i][j] == "(" = opt(i + 1, j, k + 1) or opt(i, j + 1, k + 1)
#              | otherwise = opt(i + 1, j, k - 1) or opt(i, j + 1, k - 1)

# No. states = m * n * (m + n)
# Time complexity per state -> O(1)
# Total time complexity => O(mn(m + n))

# By using bottom-up iterative dynamic programming we can reduce the
# space complexity to O(n(m + n))!