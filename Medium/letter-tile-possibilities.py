# Author: Runar Fosse
# Time complexity: O(2^n)
# Space complexity: O(n)

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        # Using backtracking

        # Count the frequency of each letter
        frequencies = [0] * 26
        indexOf = lambda c: ord(c) - ord("A")
        for letter in tiles:
            frequencies[indexOf(letter)] += 1
        
        # Then compute the total number of sequences
        return self.computeSequences(frequencies)
    
    def computeSequences(self, frequencies: List[int]) -> int:
        # Try to add one of each letters
        sequences = 0
        for c in range(26):
            if not frequencies[c]:
                continue
            
            # Remove one occurence of the letter
            frequencies[c] -= 1
            
            # Count current sequence up to now, and deepen search
            sequences += 1 + self.computeSequences(frequencies)

            # Add it back, and continue
            frequencies[c] += 1
        
        # Finally, return all sequences
        return sequences
        