# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def maxOperations(self, s: str) -> int:
        # Keep track of maximum number of operations, as well as encountered 1s
        operations, ones = 0, 0
        
        # Iterate the array from the left
        i, n = 0, len(s)
        while i < n:
            # If we encounter a 0, move every previous 1 to the right in one fell swoop
            if s[i] == "0":
                while i + 1 < n and s[i + 1] == "0":
                    i += 1
                operations += ones
            else:
                # Otherwise, count a 1
                ones += 1
            i += 1
        
        # Finally, return the maximum number of operations
        return operations
    
# We know that we have to move every 1 over every 0 to its right.
# This can be solved easily by iterating the array from the left, and keeping
# count of how many 1s we have to move over each encountered 0.