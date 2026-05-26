# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        # Store seen upper and lower characters
        lowers, uppers = [False] * 26, [False] * 26
        indexOf = lambda c: ord(c) - ord("a")

        # Iterate the word
        specials = [False] * 26
        for c in word:
            # Get the index of the current character
            index = indexOf(c.lower())

            # Mark the specific character as seen
            if c.islower():
                lowers[index] = True
            else:
                uppers[index] = True
            
            # Then, check if both versions are seen
            if lowers[index] and uppers[index]:
                # Count as special
                specials[index] = True
        
        # Finally, count and return all special characters
        return sum(1 if seen else 0 for seen in specials)
