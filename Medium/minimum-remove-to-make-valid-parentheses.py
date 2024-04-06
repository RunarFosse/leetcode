# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # Using stack
        stack, depth = [], 0

        # Add valid parantheses from the left
        for c in s:
            if c == ")":
                if depth == 0:
                    continue
                depth -= 1
            elif c == "(":
                depth += 1

            stack.append(c)
        
        # Iterate stack from the right
        for i in reversed(range(len(stack))):
            if depth == 0:
                break

            # Remove right parantheses making string invalid
            if stack[i] == "(":
                depth -= 1
                stack[i] = ""
        
        return "".join(stack)