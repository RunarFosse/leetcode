# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # Store the frequency of the characters in the word 'balloon'
        frequencies = {}
        for c in "balloon":
            # Also store multiplicity of the character
            if c not in frequencies:
                frequencies[c] = [0, 0]
            frequencies[c][1] += 1

        # Then, iterate the text, counting character frequencies
        for c in text:
            if c in frequencies:
                frequencies[c][0] += 1

        # Then, iterate the characters again
        maximum = 1e9
        for frequency, multiplicity in frequencies.values():
            # Using multiplicity to store maximum number of words to create
            maximum = min(frequency // multiplicity, maximum)
        
        # Finally, return this maximum number of 'balloon's to generate
        return maximum
