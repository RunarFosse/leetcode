# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # Using greedy
        points.sort(key=lambda p : p[1])

        # Shot an arrow at the first end position
        shots, last_arrow = 0, None
        for start, end in points:
            if not last_arrow or last_arrow < start:
                last_arrow = end
                shots += 1

        # Return the number of shots taken
        return shots
        
# We can greedily sort the points list by end time, and shoot the first balloon 
# at its last position (x_end_0), and check how many balloons popped.
#  Then we do the same for the rest, until we've reached the end of the list.