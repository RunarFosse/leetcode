# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def possibleStringCount(self, word: str) -> int:
        # Iterate the word
        originals, current = 0, (None, 1)
        for c in word:
            if c == current[0]:
                # Keep counting current character
                current = (c, current[1] + 1)
            else:
                # Otherwise, count number of ways this substring could've been typed
                originals += current[1] - 1

                # And count new character
                current = (c, 1)
        
        # Finally, return all ways string could've been typed
        return originals + current[1]