# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        # Iterate the string
        score, depth, last = 0, 0, ""
        for c in s:
            # If we find an open parenthesis, increment the depth
            if c == "(":
                depth += 1
            else:
                # Otherwise, decrement the depth
                depth -= 1

                # If the last character we've seen is an open parenthesis
                if last == "(":
                    # Then we directly compute the total score addition from this pair
                    score += 1 << depth
            
            # Updating the current last character
            last = c

        # And return the total score of the string
        return score
