# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        # Keep track of next index to insert space
        spaceIndex = 0

        # Duplicate string, with added spaces
        string = []
        for i, c in enumerate(s):
            if spaceIndex < len(spaces) and i == spaces[spaceIndex]:
                string.append(" ")
                spaceIndex += 1
            string.append(c)
        
        # Return the new string
        return "".join(string)
