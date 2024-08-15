# Author: Runar Fosse
# Time complexity: O(1)
# Space complexity: O(1)

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        # Using analytical solution
        return numBottles + (numBottles - 1) // (numExchange - 1)
    
# We know that we start with numBottles bottles of water to drink.
# The number of exchanged water bottles can be calculated like this:

# Instead of thinking that we exchange numExchange empty bottles for a new
# filled water bottle, we can think of removing (numExchange - 1) bottles
# for a free refill on the last bottle!

# In this way, the number of free bottles of water we get will be equal to
# how many times we can remove (numExchange - 1) from our bottle collection,
# always keeping one bottle as a refillable. This bottle collection
# will thus be equal to (numBottles - 1) (as 1 is our refillable!).

# This gives us the solution of how many water bottles we drink:
# numBottles + (numBottles - 1) // (numExchange - 1)