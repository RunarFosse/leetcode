# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(mn)

class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        # Using greedy
        m, n = len(land), len(land[0])
        farmlands = []

        # Iterate every grid cell
        for i in range(m):
            for j in range(n):
                # If we find a farmland, calculate bounds greedily
                if land[i][j]:
                    # Iterate and mark whole farmland as seen (to 0)
                    y, x = i, j
                    for y in range(i, m):
                        if not land[y][j]:
                            y -= 1
                            break
                        for x in range(j, n):
                            if not land[y][x]:
                                x -= 1
                                break
                            land[y][x] = 0
                            
                    # Store corners to farmlands
                    farmlands.append([i, j, y, x])
        
        # Return all pieces of farmland
        return farmlands
