# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        # Using sliding window

        # Iterate the string
        beautiful, window = inf, 0
        for c in s:
            # Expand the window
            window <<= 1
            if c == "1":
                window |= 1
            
            # If the window contains more than k set bits, shrink it
            if window.bit_count() > k:
                leftmost = (1 << (window.bit_length() - 1))
                window ^= leftmost
            
            # If the current window has exactly k set bits
            if window.bit_count() == k:
                # Store the lexicographically smallest one
                beautiful = min(window, beautiful)
        
        # If we have no beautiful string, return the empty string
        if beautiful == inf:
            return ""
        
        # Otherwise, return the lexicopgrahically smallest beautiful string
        return format(beautiful, "b")
