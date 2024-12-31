# Author: Runar Fosse
# Time complexity: O(n^2)
# Space complexity: O(n)

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # Using dynamic programming
        self.days, self.n, self.costs = days, len(days), costs
        return self.opt(0)
    
    @functools.cache
    def opt(self, i: int) -> int:
        if i == self.n:
            return 0
        
        # Compute the cost of buying a 1-day pass
        j = i + 1
        one_cost = self.costs[0] + self.opt(j)

        # A 7-day pass
        while j < self.n and self.days[j] < self.days[i] + 7:
            j += 1
        seven_cost = self.costs[1] + self.opt(j)

        # And a 30-day pass
        while j < self.n and self.days[j] < self.days[i] + 30:
            j += 1
        thirty_cost = self.costs[2] + self.opt(j)
        
        # And return the minimum
        return min(one_cost, seven_cost, thirty_cost)
        
# N.o. states = n
# Runtime per state = O(n)