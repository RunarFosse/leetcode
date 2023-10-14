# Author: Runar Fosse
# Time complexity: O(n^2)
# Space complexity: O(n)

class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        # Using bottom-up dynamic programming
        n = len(cost)
        opt = [0] + [1e9] * n

        for j in range(n):
            for i in range(n, 0, -1):
                opt[i] = min(opt[i], opt[max(i-1-time[j], 0)] + cost[j])
        
        return opt[n]
    
# At each step, either the paint painter can paint, or the free painter
# This can be re-thought as either the paid painter paints, or he doesn't
# Then:
# opt[i] - optimal cost painting i-walls

# Base case:
# opt[0] = 0
# opt[i] = infinity

# Recurrency:
# For each wall j:
# opt[i] = min(
#   opt[i] -> do not paint this wall (paint others instead), 
#   opt[i-1-time[j]] + cost[j] -> paint this wall (and i-1 others)
#)

# N.o. states = n, runtime = O(n^2) (nested for-loop)