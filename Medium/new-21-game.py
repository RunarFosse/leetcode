# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        # Using sliding window
        opt = [0.0] * (n + 1)
        opt[0] = 1.0

        # Early break if solution is trivial
        if not k or k + maxPts < n:
            return 1.0

        # Keep track of previous maxPts probabilities in a window
        window = 1.0

        # Then, iterate every possible point
        for i in range(1, n + 1):
            # Compute the probability of hitting this amount of points
            opt[i] = window / maxPts

            # Add to window if we are below k (and thus can continue drawing cards)
            if i < k:
                window += opt[i]
            
            # And remove probabilities that are out of reach
            if i - maxPts >= 0:
                window -= opt[i - maxPts]
        
        # Finally, return the probability for hitting any value between [k, n)
        return sum(opt[k:])