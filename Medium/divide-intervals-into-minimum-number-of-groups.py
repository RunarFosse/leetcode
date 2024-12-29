# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        # Store and sort start and end times in ascending order
        starts = sorted(start for start, _ in intervals)
        ends = sorted(end for _, end in intervals)

        # Store the current number of groups, and a pointer 
        # to the current non-intersecting end interval
        groups, pointer = 0, 0

        # Iterate every start time
        for start in starts:
            # If it intersects with the current end, add a group
            if start <= ends[pointer]:
                groups += 1
                continue
            
            # Otherwise increment current end pointer
            pointer += 1

        # At last, return the number of groups
        return groups 
    