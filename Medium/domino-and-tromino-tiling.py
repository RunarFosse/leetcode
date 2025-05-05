# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def numTilings(self, n: int) -> int:
        # Solve for base cases
        if n <= 1:
            return n
        
        # Iteratively solve others
        previous = (0, 1, 1)
        for i in range(2, n + 1):
            # Compute the current number of tilings
            current = (2 * previous[2] + previous[0]) % int(1e9 + 7)

            # And update the previous values
            previous = (previous[1], previous[2], current)

        # Finally, return number of tilings
        return current