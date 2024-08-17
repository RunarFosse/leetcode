# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(n)

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # Using dynamic programming
        m, n = len(points), len(points[0])

        opt = [0] * n
        for i in reversed(range(m)):
            # Store a temporary version of the last row
            last_opt = opt.copy()

            # Perform left-to-right pass
            current_max = 0
            for j in range(n):
                current_max = max(last_opt[j], current_max - 1)
                opt[j] = current_max
            
            # Perform right-to-left pass
            current_max = 0
            for j in reversed(range(n)):
                current_max = max(last_opt[j], current_max - 1)
                opt[j] = max(current_max, opt[j])

                # And at last, add each cell's point value
                opt[j] += points[i][j]

        # Return the starting cell with the highest amount of points
        return max(opt)


# opt(i, j) - The maximum number of points which can be gotten, starting 
#             from row i, column j.

# Base case:
# opt(m-1, j) = points[m-1][j]

# Recurrency:
# opt(i, j) = points[i][j] + max(opt[i+1][k] - abs(j - k) for k in range(n))

# This dp can be solved iteratively, saving a dimension of storage by
# calculating each row from m-1 to 0.

# The max operation can also be solved by a left-and-right pass over each
# column in the current row, keeping count of a current running max value.
# This also reduces the runtime by a dimension.

# N.o. states = mn
# Runtime per state = 1
# Total time complexity => O(mn)
# Space complexity => O(n) (as we iteratively compute every row)