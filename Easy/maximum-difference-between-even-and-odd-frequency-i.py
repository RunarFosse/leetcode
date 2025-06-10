# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def maxDifference(self, s: str) -> int:
        # Count frequency of each character
        indexOf = lambda c: ord(c) - ord("a")
        frequencies = [0] * 26
        for c in s:
            frequencies[indexOf(c)] += 1
        
        # Iterate the frequencies
        odd, even = 0, 1e9
        for frequency in frequencies:
            if not frequency:
                continue
            
            # Storing largest odd frequency, smallest even frequency
            if frequency % 2:
                odd = max(frequency, odd)
            else:
                even = min(frequency, even)

        # Return the maximum difference
        return odd - even