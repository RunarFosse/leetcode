# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        # Using greedy

        # Sort the costs in descending order
        cost.sort(reverse=True)

        # In distinct pairs of three, iterate the candies
        total = 0
        for candies in batched(cost, 3):
            # Buy the most and second-most expensive candy not yet bought
            total += candies[0]
            if len(candies) > 1:
                total += candies[1]

            # Leaving the third-most expensive to be taken for free
        
        # Finally, return the minimum total cost buying all candies
        return total
