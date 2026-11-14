# Author: Runar Fosse
# Time complexity: O(1)
# Space complexity: O(1)

class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        # Compute the amount of both items we need
        needBoth = min(need1, need2)

        # And buy either both together, or separately
        cost = min(costBoth * needBoth, (cost1 + cost2) * needBoth)

        # Then, buy the remaining items, either with its own cost, or with the combined
        if need1 > need2:
            cost += min(cost1 * (need1 - needBoth), costBoth * (need1 - needBoth))
        else:
            cost += min(cost2 * (need2 - needBoth), costBoth * (need2 - needBoth))
        
        # This is the minimum cost required to buy all needed items
        return cost
