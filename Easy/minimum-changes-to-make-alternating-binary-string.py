# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)

        # Assume the first bit should be 0, and count operations
        operations = 0
        for i in range(n):
            # Should flip bit
            if (i % 2 and s[i] == '0') or (not i % 2 and s[i] == '1'):
                operations += 1
        
        # Return minimum number of operations, depending on actual starting bit
        return min(operations, n - operations)


# We start by assuming the first bit should be 0, and then count the operations to
# make the string alternating. However, by symmetry, if the first bit should be 1, then
# the operations to make the string alternating would be equal to:
# length of string - number of operations if the first bit is 0.

# Therefore, the minimum number of operations will be equal to:

# min (number of operations if first is 0, length s - number of operations if first is 0)