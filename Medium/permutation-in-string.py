# Author: Runar Fosse
# Time complexity: O(m + n)
# Space complexity: O(1)

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Using sliding window

        # Compute frequencies of characters in the first string
        indexOf = lambda c: ord(c) - ord("a")
        frequencies = [0] * 26
        for c in s1:
            frequencies[indexOf(c)] += 1
        
        # Then slide over the second string
        start, window_frequencies = 0, [0] * 26
        for c in s2:
            # Expand the window
            window_frequencies[indexOf(c)] += 1

            # While any character appears more in window than in s1, shrink
            while window_frequencies[indexOf(c)] > frequencies[indexOf(c)]:
                window_frequencies[indexOf(s2[start])] -= 1
                start += 1
            
            # If the current letter appears exactly as any times in window,
            # as in s1, check if the rest also does
            if window_frequencies[indexOf(c)] == frequencies[indexOf(c)]:
                is_permutation = all(
                    window_frequencies[c] == frequencies[c] 
                    for c in range(26))
                if is_permutation:
                    return True
        
        # If loop terminates, s2 does not contain a permutation of s1
        return False