# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        # Using sliding window
        n = len(s)

        # Compute the total frequency of each of the characters
        frequencies = [0] * 3
        indexOf = lambda c: ord(c) - ord("a")
        for c in s:
            frequencies[indexOf(c)] += 1
        
        # If any characters appear less than k times, it is impossible to take k of each
        if min(frequencies) < k:
            return -1
        
        # Otherwise, slide a window over the string
        time, start = n, 0
        for end in range(n):
            # Expand + shrink the window, if outside does not contain at least k of each
            frequencies[indexOf(s[end])] -= 1
            while min(frequencies) < k:
                frequencies[indexOf(s[start])] += 1
                start += 1
            
            # Then store minimum time
            time = min(n - (end - start + 1), time)
        
        # And finally, return said minimum time
        return time
