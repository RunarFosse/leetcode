# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def minSwaps(self, s: str) -> int:
        # Iterate the string and count unmatched open brackets
        unmatched = 0
        for c in s:
            if c == "[":
                unmatched += 1
            elif unmatched:
                unmatched -= 1
            
        # The number of swaps is now half the number of unmatched brackets
        return ceil(unmatched / 2)
