# Author: Runar Fosse
# Time complexity: O(nk)
# Space complexity: O(1)

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        indexOf = lambda c : ord(c) - ord('a')

        # Count char frequency
        frequencies = [0 for _ in range(26)]
        for word in words:
            for c in word:
                frequencies[indexOf(c)] += 1
        
        # Verify divisibility
        for frequency in frequencies:
            if frequency % len(words):
                return False
        
        return True

# Count each letter frequency and check if they all are divisible by
# the length of the words array. If so return true, else false.

# As words[i] consists only of lowercase english letters (26), we could do this
# in constant auxillary space.