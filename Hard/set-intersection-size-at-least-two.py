# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        # Using greedy

        # Sort the intervals in order of ascending end, descending start
        intervals.sort(key=lambda e: (e[1], -e[0]))

        # Perform a linear scan, tracking overlap with two largest elements
        containing, overlap = 0, None
        for start, end in intervals:
            # If the current interval does not overlap
            if not overlap or start > overlap[1]:
                # Add the two largest elements to the containing set
                overlap = (end - 1, end)
                containing += 2
            
            # However, if they partially overlap, update largest overlapping element
            elif start > overlap[0]:
                overlap = (overlap[1], end)
                containing += 1
        
        # Finally, return the size of the smallest overlapping set
        return containing
        