# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def makeGood(self, s: str) -> str:
        # Using stack
        n = len(s)

        # Declare a function for deciding if two characters makes a string bad
        def makes_string_bad(c1: str, c2: str) -> bool:
            if c1.islower():
                return c2.isupper() and c1 == c2.lower()
            return c2.islower() and c1 == c2.upper()

        # Iterate the string
        stack = []
        for i in range(n):
            # Check if current stored string will be bad
            if stack and makes_string_bad(stack[-1], s[i]):
                # If so, remove the last character from stack
                stack.pop()
            
            else:
                # If not, add the current one
                stack.append(s[i])

        # Return the great string
        return "".join(stack)