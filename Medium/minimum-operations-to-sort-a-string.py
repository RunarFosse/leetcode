# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)

        # If the string contains at at most two elements
        if n <= 2:
            # We cannot perform any operations to it
            return 0 if s[0] <= s[-1] else -1
        
        # Otherwise, check if the array is already sorted
        descents, maximum, minimum = 0, s[0], s[0]
        for i in range(1, n):
            if s[i] < s[i - 1]:
                descents += 1
            
            # Also store maximum and minimum characters
            maximum = max(s[i], maximum)
            minimum = min(s[i], minimum)
        
        # If it is, we don't need to apply any operations
        if descents == 0:
            return 0
        
        # If the minimum or the maximum is in the correct spot
        if s[0] == minimum or s[-1] == maximum:
            # We can sort the rest of the array in 1 operation
            return 1
        
        # Otherwise, we need to correctly place both extremal elements
        operations = 2

        # Count occurences of minimal and maximum elements
        maximums, minimums = 0, 0
        for i in range(n):
            if s[i] == maximum:
                maximums += 1
            if s[i] == minimum:
                minimums += 1
        
        # If both the minimum and maximum elements are only placed at the wrong corner
        if s[-1] == minimum and s[0] == maximum and max(minimums, maximums) == 1:
            # We need one extra substring sort to place both correctly
            operations += 1

        # Finally, return the number of substring sorts to sort the whole string
        return operations
