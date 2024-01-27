# Author: Runar Fosse
# Time complexity: O(nk)
# Space complexity: O(k)

class Solution:
    mod = int(1e9 + 7)
    def kInversePairs(self, n: int, k: int) -> int:
        # Using dynamic programming
        last = [1] + [0] * k

        # Iterate over every array size up until n
        for i in range(1, n+1):
            current = [1] + [0] * k
            # Iterate over every inversion count
            for j in range(1, k+1):
                # Let current be a sliding window of n-sized slice of last row
                # And add/remove accordingly
                current[j] = (current[j-1] + last[j]) % self.mod
                if j >= i:
                    current[j] = (current[j] - last[j - i]) % self.mod
                
            # Replace last row with current
            last = current

        return current[k]


# opt(n, k) - number of arrays of size n with k inversions

# Base case:
# opt(n, 0) = 1
# opt(0, k) = 0

# Recurrency:
# opt(n, k) = sum(opt(n - 1, k - inversions) for inversions in n)

# With optimized space we store 2 rows at a time instead of n.

# N.o. states = k, runtime per state = O(n)
# Final tc O(nk)