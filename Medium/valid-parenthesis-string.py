# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def checkValidString(self, s: str) -> bool:
        # Store an interval of consisting of current
        # possible open parenthesis pairs
        min_open, max_open = 0, 0

        # Then iterate string, updating interval on the fly
        for c in s:
            if c == "(":
                min_open += 1
                max_open += 1
            elif c == ")":
                min_open -= 1
                max_open -= 1
            else:
                min_open -= 1
                max_open += 1
            
            # As minimum open pairs can never be negative, clamp to 0
            if min_open < 0:
                min_open = 0

            # If maximimum open pairs every becomes negative, we have closed
            # more parentheses than possibly opened, i.e. an invalid string
            if max_open < 0:
                return False

        # The string is valid if the minimum possible open pairs is 0
        return not min_open