# Author: Runar Fosse
# Time complexity: O(n^2)
# Space complexity: O(n^2)

class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        # Using dynamic programming
        self.cost = cost
        self.time = time
        return self.opt(0, 0)

    @functools.cache
    def opt(self, i: int, j: int) -> int:
        if i >= len(self.cost):
            return 0 if j >= 0 else 1e9
        if j > len(self.cost) - i:
            return 0
        
        return min(self.cost[i] + self.opt(i+1, j+self.time[i]), self.opt(i+1, j-1))

    
# At each step, either the paint painter can paint, or the free painter

# opt(i, j) - optimal cost at index i, where j is time free painter can paint

# Base case:
# opt(n, j) = 0 if j >= 0 else infinity
# opt(i, j > (n-i)) = 0   # If paid painter is used for more than the remaining
                          # time, free painter can take care of the rest

# Recurrency:
# opt(i, j) = min (
#    cost[i] + opt(i+1, j+time[i]),
#    opt(i+1, j-1)
#)

# N.o. states = n^2, runtime per state: O(1)
# --> Time complexity of O(n^2)