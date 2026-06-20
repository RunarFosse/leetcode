# Author: Runar Fosse
# Time complexity: O(mlog m)
# Space complexity: O(m)

class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        # Using greedy

        # First, add a restriction to the initial building
        restrictions.append([1, 0])

        # Then, sort the restrictions by ascending order of id
        restrictions.sort()

        # Also, if it doesn't exist, add a final restriction denoting total build limit
        if restrictions[-1][0] != n:
            restrictions.append([n, n - 1])
        
        # Then, perform a left-to-right pass of the restrictions
        m = len(restrictions)
        for i in range(m - 1):
            # Ensuring that the next build limit is reachable from the current
            buildings = restrictions[i + 1][0] - restrictions[i][0]
            restrictions[i + 1][1] = min(restrictions[i][1] + buildings, restrictions[i + 1][1])
        
        # Then do the same, just right-to-left
        for i in reversed(range(1, m)):
            buildings = restrictions[i][0] - restrictions[i - 1][0]
            restrictions[i - 1][1] = min(restrictions[i][1] + buildings, restrictions[i - 1][1])

        # Finally, iterate the building restrictions in pairs
        maximum = 0
        for building1, building2 in pairwise(restrictions):
            # Compute the height of the peak building between
            buildings = building2[0] - building1[0]
            height = (buildings + building1[1] + building2[1]) // 2

            # Store the maximum possible building height
            maximum = max(height, maximum)
        
        # And finally, return this maximum possible build height
        return maximum
