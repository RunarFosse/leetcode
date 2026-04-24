# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        # Using greedy
        n = len(moves)

        # First, count the number of Ls and Rs
        lefts, rights = 0, 0
        for move in moves:
            match move:
                case "L":
                    lefts += 1
                case "R":
                    rights += 1
        
        # Then, add all wildcard moves to the maximal direction
        wildcards = n - (lefts + rights)
        if lefts > rights:
            lefts += wildcards
        else:
            rights += wildcards
        
        # Finally, return the furthest possible final position
        return abs(lefts - rights)
