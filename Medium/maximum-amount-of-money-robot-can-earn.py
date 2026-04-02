# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(mn)

class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        # Using dynamic programming
        m, n = len(coins), len(coins[0])
        opt = [[[-int(1e9)] * 3 for _ in range(n + 1)] for _ in range(m + 1)]

        # Denote the valid base cases
        opt[m - 1][n] = [0] * 3
        opt[m][n - 1] = [0] * 3
        
        # Iterate all the tiles
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                for k in range(3):
                    # Grab the amount of money on the current tile and continue
                    money = coins[i][j] + max(opt[i + 1][j][k], opt[i][j + 1][k])

                    # However if there is a robber, try to neutralize him, if possible
                    if coins[i][j] < 0 and k > 0:
                        money = max(opt[i + 1][j][k - 1], opt[i][j + 1][k - 1], money)
                    
                    opt[i][j][k] = money

        return max(opt[0][0])


# opt(i, j, k) - The maximum amount of money a robot can earn starting at (i, j),
#                with k robber neutralizations remaining

# Base case:
# opt(m, j, k) = 0 if j == n - 1 else -inf
# opt(i, n, k) = 0 if i == m - 1 else -inf
# opt(_, _, -1) = -inf

# Recurrency:
# opt(i, j, k) = max(
#                   coins[i][j] + max(opt(i + 1, j, k), opt(i, j + 1, k)),
#                   opt(i + 1, j, k - 1), opt(i, j + 1, k - 1)
#               )

# N.o. states = m*n*2
# Time complexity per state -> O(1)
# Total time complexity => O(mn)