# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n, i = len(intervals), 0
        newIntervals = []

        # First add all which end before newInterval starts
        while i < n and intervals[i][1] < newInterval[0]:
            newIntervals.append(intervals[i])
            i += 1
        
        # Then merge all that has to and add
        while i < n and (intervals[i][1] >= newInterval[0] and intervals[i][0] <= newInterval[1]):
            newInterval = (min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1]))
            i += 1
        newIntervals.append(newInterval)

        # Then finally add the remaining
        while i < n:
            newIntervals.append(intervals[i])
            i += 1
        
        # And return the resulting interval list
        return newIntervals