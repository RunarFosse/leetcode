# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        # Using greedy
        n = len(s)

        # First, compute the sum of the whole string
        value = reduce(lambda r, e: 2*r + int(e), s, 0)

        # Then iterate the string from the left
        removed = 0
        for i in range(n):
            # Break if value is smaller or equal to k
            if value <= k:
                break

            # Otherwise, greedily remove the largest set bits
            if s[i] == "1":
                value ^= 1 << (n - i - 1)
                removed += 1
            
        # Finally, return the length of this substring
        return n - removed