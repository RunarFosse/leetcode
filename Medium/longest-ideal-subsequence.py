# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        # Using dynamic programming
        n = len(s)
        result = 0

        # Iterate whole string
        opt = [0] * 26
        for c in reversed(s):
            current = ord(c) - ord("a")

            # Find longest ideal subsequence given current char
            longest_suffix = max(opt[next] for next in range(26) if abs(current - next) <= k)
            
            # Add current char to said subsequence
            opt[current] = longest_suffix + 1
            
            # Also store the current longest
            result = max(opt[current], result)
        
        # Return the longest ideal subsequence out of all possible
        return result

# opt(c) - Longest ideal subsequence which starts with character c

# Iterate whole string (from right-to-left), storing length of longest
# ideal subsequence starting at a given character. Then we update the stored
# value for the current character by finding the max size of all characters,
# within bounds k.
