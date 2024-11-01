# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def makeFancyString(self, s: str) -> str:
        # Iterate the string
        stack = []
        for c in s:
            # Skip if the current letter has occured thrice consecutively
            if len(stack) > 1 and c == stack[-1] == stack[-2]:
                continue
            # Append it to the stack
            stack.append(c)
        
        # At last, return the fancy string
        return "".join(stack)
            