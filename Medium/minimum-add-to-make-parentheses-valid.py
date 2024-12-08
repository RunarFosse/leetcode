# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opened, missing = 0, 0
        for c in s:
            # Increment open paranthesis count
            if c == "(":
                opened += 1
            # Decrement open count if there exist any unclosed
            elif c == ")" and opened:
                opened -= 1
            # If not, count it as closed but not opened
            else:
                missing += 1

        # Return all opened but not closed, and closed but not opened
        return opened + missing