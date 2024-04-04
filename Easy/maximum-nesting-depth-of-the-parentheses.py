# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def maxDepth(self, s: str) -> int:
        n = len(s)

        # Calculate deepest nesting of parantheses
        depth, max_depth = 0, 0
        for i in range(n):
            match s[i]:
                case "(":
                    depth += 1
                    max_depth = max(depth, max_depth)
                case ")":
                    depth -= 1
        
        return max_depth