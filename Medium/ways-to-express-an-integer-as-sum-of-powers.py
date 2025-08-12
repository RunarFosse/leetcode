# Author: Runar Fosse
# Time complexity: O(n^2)
# Space complexity: O(n)

class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        # Using dynamic programming
        mod = int(1e9) + 7
        
        # Compute this, bottom-up
        opt = [0] * (n + 1)
        opt[0] = 1

        # For each positive integer i
        for i in range(1, n + 1):
            # Store a temp array of opt
            temp = opt[:]

            # Compute i's x-th power
            power = pow(i, x)

            # And compute ways to calculate j with or without i^x
            for j in range(n + 1):
                # Either by skipping, or if possible, picking 
                opt[j] = temp[j] + (0 if power > j else temp[j - power])
                opt[j] %= mod
        
        # Finally, return the number of ways to compute n
        return opt[n]