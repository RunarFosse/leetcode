# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        
        # Compute weight of adjacent marbles and sort them in ascending order
        adjacents = sorted([weights[i] + weights[i + 1] for i in range(n - 1)])

        # Then, for each of the k - 1 split indices
        difference = 0
        for i in range(k - 1):
            # Compute the difference between the maximum and minimum cost
            difference += adjacents[n - i - 2] - adjacents[i]
        
        # Finally, return that difference
        return difference

# Splitting marbles into k bags mean we have k - 1 split indices, where the cost
# of a distribution is equal to the first and last marbles plus the marbles
# adjacent to each split index.