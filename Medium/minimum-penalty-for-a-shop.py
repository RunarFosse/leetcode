# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        # Using prefix sum
        n = len(customers)

        # Iterate the array
        earliest, penalty, prefix = 0, 0, 0
        for i in range(n):
            # Computing penalty for staying open on the fly
            prefix += 1 if customers[i] == "N" else -1

            # If the penalty is minimum, store this as earliest hour to close
            if prefix < penalty:
                penalty = prefix
                earliest = i + 1
        
        # Finally, return said earliest time to close
        return earliest

# Instead of computing penalty before AND after closing, we can optimize by only
# computing the penalty before. This will be proportional to the total penalty,
# and can be used to find the optimal hour to close!