# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Using greedy
        difference, min_price = 0, prices[0]
        for price in prices:
            difference = max(price - min_price, difference)
            min_price = min(price, min_price)
        
        return difference
        
# This can easily be solved greedily. Pick the two days with the highest difference
# in price, i.e. pick the minimum, computing the difference for each maximum,
# whilst iterating the prices array from left to right.