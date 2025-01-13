# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def minimumLength(self, s: str) -> int:
        # Compute the frequency of each letter
        frequencies = [0] * 26
        indexOf = lambda c: ord(c) - ord("a")
        for c in s:
            frequencies[indexOf(c)] += 1
        
        # Then compute and return length after performing all operations
        result = 0
        for frequency in frequencies:
            if not frequency:
                continue
                
            result += 1 if frequency % 2 else 2
        return result
