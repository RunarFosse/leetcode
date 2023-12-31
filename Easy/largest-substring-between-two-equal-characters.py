# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        # Store first and last occurence
        indexOf = lambda c : ord(c) - ord('a')
        occurences = [(-1, -1) for _ in range(26)]
        for i, c in enumerate(s):
            index = indexOf(c)
            if occurences[index][0] == -1:
                occurences[index] = (i, -1)
            else:
                occurences[index] = (occurences[index][0], i)

        # Return largest occurence difference
        return max(last-first-1 for first, last in occurences)
        
        

# For each character in the array, we store the first and last occurence.
# Then we can iterate this array, returning the maximum difference.

# This is space O(1) as s contains only lowercase english letters.