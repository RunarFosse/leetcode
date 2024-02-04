# Author: Runar Fosse
# Time complexity: O(nk)
# Space complexity: O(n)

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        # Using dynamic programming
        n = len(arr)
        opt = [0] * (n+1)

        for i in reversed(range(n)):
            # Keep track of current max within window
            current_max = arr[i]

            # For each possible window size
            for j in range(1, k+1):
                # Calculate maximum sum after partitioning
                opt[i] = max(current_max * j + opt[i+j], opt[i])

                if i+j == n:
                    break
                current_max = max(arr[i+j], current_max)
        
        return opt[0]


# opt(i) - Maximum sum of partitioned array for the subarray arr[i:]

# Base case:
# opt(n) = 0

# Recurrency:
# opt(i) = max( opt(i + j) + max(arr[i:i+j+1]) * j for j in [1..k] )

# n.o. states = n, runtime per state = O(k)