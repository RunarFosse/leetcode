# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Using Dynamic programming
        self.cost = cost
        return min(self.opt(0), self.opt(1))
    
    @functools.cache
    def opt(self, i: int) -> int:
        if i >= len(self.cost):
            return 0
        
        return min(self.opt(i+1), self.opt(i+2)) + self.cost[i]


# opt(i) is minimum cost from index i to the top floor

# Base case:
# opt(n) = 0

# Recurrency:
# opt(i) = min(opt(i+1), opt(i+2)) + cost[i]

# N.o. states = n, runtime per state = O(1)
# Time complexity => O(n)