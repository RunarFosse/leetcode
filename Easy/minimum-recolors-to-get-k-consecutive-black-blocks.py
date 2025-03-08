# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # Using sliding window
        n = len(blocks)

        # Iterate the string
        start = 0
        min_recolors, recolors = 1e9, 0
        for i in range(n):
            # If the next value in the window is white
            if blocks[i] == "W":
                # Recolor
                recolors += 1
            
            # If window contains k elements
            if i + 1 - start == k:
                # Store minimum number of recolors
                min_recolors = min(recolors, min_recolors)

                # And move start pointer one index
                if blocks[start] == "W":
                    recolors -= 1
                start += 1
        
        # Return the minimum number of recolors
        return min_recolors