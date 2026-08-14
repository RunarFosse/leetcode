# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        # Using sliding window
        n = len(s)

        # Store the frequencies of each character
        frequencies = [0] * 26
        indexOf = lambda c: ord(c) - ord("a")

        # And slide a window over the string
        longest, start = 0, 0
        for end in range(n):
            # Expand the window
            frequencies[indexOf(s[end])] += 1

            # Shrink the window if it contains more than two of this character
            while frequencies[indexOf(s[end])] > 2:
                frequencies[indexOf(s[start])] -= 1
                start += 1
            
            # And store the longest
            longest = max(end - start + 1, longest)
        
        # Finally, return the length of the longest such substring
        return longest
