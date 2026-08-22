# Author: Runar Fosse
# Time complexity: O(n^2)
# Space complexity: O(n^2)

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        # Using dynamic programming
        n = len(stoneValue)
        
        # Store the maximum values Alice can get by keeping a left/right interval
        maxLeft, maxRight = [[0] * n for _ in range(n)], [[0] * n for _ in range(n)]

        # And compute the best scores Alice can obtain from any interval
        opt = [[0] * n for _ in range(n)]
        for start in reversed(range(n)):
            total, prefix = stoneValue[start], 0
            maxLeft[start][start] = maxRight[start][start] = total

            # Keep track of the monotonic split index i
            i = start - 1
            for end in range(start + 1, n):
                total += stoneValue[end]

                # Move i until it reaches critical split
                while i + 1 < end and (prefix + stoneValue[i + 1]) * 2 <= total:
                    prefix += stoneValue[i + 1]
                    i += 1
                
                # And store optimal scores for Alice, by keeping either interval
                if start <= i:
                    opt[start][end] = max(maxLeft[start][i], opt[start][end])
                if i + 1 < end:
                    opt[start][end] = max(maxRight[i + 2][end], opt[start][end])
                if prefix * 2 == total:
                    opt[start][end] = max(maxRight[i + 1][end], opt[start][end])
                
                # And compute maximum left/right interval scores
                score = total + opt[start][end]
                maxLeft[start][end] = max(score, maxLeft[start][end - 1])
                maxRight[start][end] = max(score, maxRight[start + 1][end])
        
        # Finally, return the maximum score Alice can obtain
        return opt[0][n - 1]


# opt(start, end) - The maximum score Alice can obtain from picking
#             stones from the interval [i, j]

# Base case:
# opt(start, start) = 0

# Recurrency:
# opt(start, end) = max(
#               opt(start, i) + prefix if prefix <= suffix,
#               opt(i + 1, end) + suffix if prefix >= suffix
#               for i in range(start, end)
#             )

# No. states = n^2
# Time complexity per state -> O(n)
# Total time complexity => O(n^3)

# By using an iterative approach, we can compute a monotonic split index for each
# start/end interval, simplifying the computation per state to amortized O(1), using
# maximum values from left side interval, and maximum values from right side interval.