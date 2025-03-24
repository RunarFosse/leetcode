# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        # Using interval scheduling

        # Sort meetings in ascending order of start time
        meetings.sort()

        # Add a faux meeting to mark the end
        meetings.append([days + 1, 0])

        # Then iterate the meetings, counting number of free days
        current, free = 0, 0
        for start, end in meetings:
            free += max(0, start - current - 1)
            current = max(end, current)
        
        # Finally, return number of free days
        return free