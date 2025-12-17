# Author: Runar Fosse
# Time complexity: O(nk)
# Space complexity: O(k)

class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        # Using dynamic programming
        n = len(prices)
        opt = [[0] * 3 for _ in range(k + 1)]

        # Initialize the prices from the first day
        for j in range(k):
            opt[j + 1][1] = -prices[0]
            opt[j + 1][2] = prices[0]
        
        # Then, iterate every following day
        for i in range(1, n):
            # Iterate every possible buy
            for j in reversed(range(k)):
                # Stop the current transactions and reap maximum profit
                profit = lambda j: max(opt[j][1] + prices[i], opt[j][2] - prices[i])
                opt[j + 1][0] = max(profit(j + 1), opt[j + 1][0])

                # Compute current balance starting a normal transaction or short
                opt[j + 1][1] = max(opt[j][0] - prices[i], opt[j + 1][1])
                opt[j + 1][2] = max(opt[j][0] + prices[i], opt[j + 1][2])
        
        # And return maximum total profit after making at most k transactions
        return opt[k][0]


# opt(k, t) - Current rolling maximum profit after doing k transactions, in a
#               current transaction type t (t=0 nothing, t=1 normal, t=2 short)

# No. states = 3 * k
# Time complexity per = O(n)
# Total time complexity -> O(nk)