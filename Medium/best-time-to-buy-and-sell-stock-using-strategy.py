# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        # Using prefix sum
        n = len(prices)

        # Compute prefix sum of prices and profits (use strategy array for profits)
        for i in range(n):
            # Profits are computed from strategy
            strategy[i] *= prices[i]
            strategy[i] += strategy[i - 1] if i else 0
            
            # Prices is a strict prefix sum
            prices[i] += prices[i - 1] if i else 0

        # Then, iterate every possible start index for modification
        maximum = strategy[-1]
        for i in range(n - k + 1):
            # And compute the maximum possible profit
            left = strategy[i - 1] if i else 0
            right = strategy[-1] - strategy[i + k - 1]
            middle = prices[i + k - 1] - prices[i + k // 2 - 1]
            maximum = max(left + middle + right, maximum)
        
        # And return this maximum possible profit
        return maximum
