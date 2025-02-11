# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(m + n)

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        # Using stack
        m = len(part)

        # Iterate the string
        stack = []
        for c in s:
            # Add the current character to the stack
            stack.append(c)

            # If the last part matches the substring, remove it
            if "".join(stack[-m:]) == part:
                for _ in range(m):
                    stack.pop()
        
        # Return the final string
        return "".join(stack)
            