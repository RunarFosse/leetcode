# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        # Iterate the string
        string, opened = [], 0
        for c in s:
            # Add the current character temporarily to the result string
            string.append(c)

            # If it is an open parenthesis
            if c == "(":
                # And it is outermost, remove it
                if opened == 0:
                    string.pop()
                opened += 1
            
            # Or if it is a closed parenthesis
            elif c == ")":
                # And it is outermost, remove it
                opened -= 1
                if opened == 0:
                    string.pop()
        
        # Finally, return the resulting string
        return "".join(string)
