# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        # Using dynamic programming

        # Create the DP array
        opt = [0, inf, inf]

        # Walk up the stairs
        for i in range(n):
            # Compute the cheapest way to get to this step
            cheapest = min(
                opt[0] + costs[i] + 1,
                opt[1] + costs[i] + 4,
                opt[2] + costs[i] + 9
            )

            # And update the DP array
            opt = [cheapest, opt[0], opt[1]]
        
        # Finally, return the minimal cost to reach the top of the staircase
        return opt[0]


# opt(i) - The minimum total cost to reach step n, starting at step i.

# Base case:
# opt(n) = 0

# Recurrency:
# opt(i) = min(
#               opt(i + 1) + costs[i] + 1,
#               opt(i + 2) + costs[i] + 4,
#               opt(i + 3) + costs[i] + 9
#          )

# No. states = n
# Time complexity per state -> O(1)
# Total time complexity => O(n)

# By utilizing bottom-up dynamic programming, we can reduce the total
# space complexity to O(1)!