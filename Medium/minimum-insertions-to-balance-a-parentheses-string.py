# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def minInsertions(self, s: str) -> int:
        # Iterate the string 
        i, n = 0, len(s)
        insertions, opened = 0, 0
        while i < n:
            # If we find an open parenthesis, count it
            if s[i] == "(":
                opened += 1
                i += 1
                continue
            
            # Otherwise, check if we have a previous opened one
            if opened > 0:
                opened -= 1
            else:
                # If not, add one
                insertions += 1
            
            # Then, check that we have two consecutive closed parentheses
            i += 1
            if i < n and s[i] == ")":
                # If so, we have a valid parenthesis pair
                i += 1
                continue
            
            # Otherwise, we need to add the remaining closed parenthesis
            insertions += 1
        
        # Finally, add the remaining missing closed parentheses
        insertions += opened * 2

        # And return the minimum insertions to balance the parentheses string
        return insertions
