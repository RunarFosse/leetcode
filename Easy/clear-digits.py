# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def clearDigits(self, s: str) -> str:
        # Using stack

        # Iterate the string
        stack = []
        for c in s:
            # If the current letter is not a character
            if not c.isdigit():
                # Add it to the stack
                stack.append(c)
                continue
            
            # Otherwise, remove the previous, if it exists
            if stack:
                stack.pop()
        
        # Finally, return the resulting string
        return "".join(stack)