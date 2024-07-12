# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        # Using greedy
        points = 0

        # Greedily count score from highest yielding substring first
        best_substr = "ab" if x > y else "ba"
        best_yield = x if x > y else y
        other_substr = "ba" if x > y else "ab"
        other_yield = y if x > y else x

        # Use a stack to keep non-removed chars
        stack = []

        # Iterate and remove best substrings
        for c in s:
            if not stack or stack[-1] + c != best_substr:
                stack.append(c)
            else:
                stack.pop()
                points += best_yield
        
        # Then do the same but for the other substring
        s, stack = stack, []
        for c in s:
            if not stack or stack[-1] + c != other_substr:
                stack.append(c)
            else:
                stack.pop()
                points += other_yield
        
        # Return total points
        return points