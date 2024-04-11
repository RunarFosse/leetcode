# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # Using monotonic stack

        # Greedily remove k digits to minimize resulting number
        stack = []
        for digit in num:
            while stack and k and digit < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(digit)
        
        # If k is not 0, pop from the end of the stack
        if k:
            stack = stack[:-k]

        # Remove leading 0s
        result = "".join(stack).lstrip("0")

        # Return result if it exists, else "0"
        return result if result else "0"
