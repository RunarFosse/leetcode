# Author: Runar Fosse
# Time complexity: O(m + n)
# Space complexity: O(m)

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        # Using greedy

        # Store the number of ice cream bars at each cost that the boy can buy
        bars = [0] * min(coins, max(costs))
        for cost in costs:
            if cost <= coins:
                bars[cost - 1] += 1
        
        # Then, iterate all of the bars
        total = 0
        for cost, amount in enumerate(bars):
            # If the boy is out of coins, break
            if (cost + 1) > coins:
                break
            
            # Otherwise, greedily buy all the cheapest possible bars
            buyable = coins // (cost + 1)
            total += min(amount, buyable)
            coins -= (cost + 1) * min(amount, buyable)
        
        # Finally, return the maximum number of ice cream bars
        return total
