# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(mn)

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        # Using two pointers
        m, n = len(box), len(box[0])

        # First rotate the box
        rotated = [[box[i][j] for i in reversed(range(m))] for j in range(n)]
        
        # From the bottom up
        for i in reversed(range(m)):
            # Store the current lowest empty position
            free = None
            for j in reversed(range(n)):
                # And simulate falling of stones 
                match rotated[j][i]:
                    case ".":
                        if not free:
                            free = j
                    case "*":
                        free = None
                    case "#":
                        if not free:
                            continue
                        rotated[j][i] = "."
                        rotated[free][i] = "#"
                        free -= 1
    
        # Finally return the fully rotated box
        return rotated