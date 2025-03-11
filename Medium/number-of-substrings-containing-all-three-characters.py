# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # Using sliding window
        n = len(s)

        # Store frequencies of chars in current substrings in an array
        indexOf = lambda c: ord(c) - ord("a")
        freqs = [0, 0, 0]

        # Slide a window over the string
        start = 0
        substrings = 0
        for i in range(n):
            freqs[indexOf(s[i])] += 1
            
            # If we have at least one of each character
            while all(freqs):
                # Count all the remaining strings
                substrings += n - i

                # And shrink the window
                freqs[indexOf(s[start])] -= 1
                start += 1
        
        # Return the number of substrings
        return substrings