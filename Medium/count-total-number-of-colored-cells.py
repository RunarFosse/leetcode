# Author: Runar Fosse
# Time complexity: O(1)
# Space complexity: O(1)

class Solution:
    def coloredCells(self, n: int) -> int:
        # Using analytical solution
        return 1 + 2 * n * (n - 1)

# We know that at n = 1, we have one square.
# Then we know that each following squares colors the touching squares.
# This means:
# 
# Step 1: 1
# Step 2: 1 + 4
# Step 3: 1 + 4 + 8
# Step 4: 1 + 4 + 8 + 12
# Step 5: 1 + 4 + 8 + 12 + 16
# 
# As we can see, this follows a pattern:
# Step n: 1 + 4 + 4*2 + 4*3 + ... + 4*(n-1)
#
# This can be rewritten in a closed form solution as:
# Step n: 1 + 4 * (sum of [1, n-1]) = 1 + 4 * (n - 1) * n / 2
#       = 1 + 2 * (n - 1) * n