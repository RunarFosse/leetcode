# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # First, count valid parentheses strings from left to right
        longest, opened, closed = 0, 0, 0
        for c in s:
            # Count opened and closed parentheses
            if c == "(":
                opened += 1
            else:
                closed += 1
            
            # If we have as many opened as closed
            if opened == closed:
                # Then count the longest well-formed parentheses string
                longest = max(opened + closed, longest)
            
            # However, if we have more closed than opened
            if opened < closed:
                # Restart counting, as current substring is ill-formed
                opened, closed = 0, 0
        
        # Lastly, perform the same pass backwards, ensuring no substring is missed
        opened, closed = 0, 0
        for c in reversed(s):
            if c == "(":
                opened += 1
            else:
                closed += 1
            if opened == closed:
                longest = max(opened + closed, longest)

            # However, backwards, we need to check if we have more opened than closed
            if opened > closed:
                # As backwards, that makes a substring ill-formed
                opened, closed = 0, 0
        
        # Finally, return the length of the longest well-formed parentheses substring
        return longest
