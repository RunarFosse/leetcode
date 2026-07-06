# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # Using greedy

        # First, sort the intervals in ascending order of left, descending order of right
        intervals.sort(key=lambda e: (e[0], -e[1]))

        # Then, iterate the intervals
        remaining, last = 0, (-1, -1)
        for interval in intervals:
            # If interval is not completely covered, keep it
            if interval[0] < last[0] or interval[1] > last[1]:
                remaining += 1
                last = interval
        
        # Finally, return the number of covered intervals
        return remaining
