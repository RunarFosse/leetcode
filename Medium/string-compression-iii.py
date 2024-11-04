# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def compressedString(self, word: str) -> str:
        n = len(word)

        # Iterate the word
        compressed, i = [], 0
        while i < n:
            c, count = word[i], 0
            # Keep track of how many letters are equal to c, at max 9
            while i < n and word[i] == c and count < 9:
                count += 1
                i += 1
            
            # Then compress this section
            compressed.append(str(count) + c)
        
        # At last, return the compressed string
        return "".join(compressed)
            