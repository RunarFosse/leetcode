# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def minimumPushes(self, word: str) -> int:
        # First count frequency of each letter
        frequencies = [0] * 26
        indexOf = lambda c : ord(c) - ord("a")
        for c in word:
            frequencies[indexOf(c)] += 1
        
        # Then sort frequencies in descending order
        frequencies.sort(reverse=True)

        # And iterate them, greedily distributing key positions
        pushes = 0
        for i in range(26):
            key_position = (i // 8 + 1)
            pushes += frequencies[i] * key_position
        
        # Return the number of pushes needed
        return pushes

# As frequency array is constant regardless of input, sorting it
# does not affect time complexity.