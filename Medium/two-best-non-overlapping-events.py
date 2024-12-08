# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        # Using binary search
        n = len(events)

        # Sort events in ascending order of start time
        events.sort()

        # Compute the maximum value of events after timesteps
        maximum_values = deque([])
        for start, _, value in reversed(events):
            maximum_value = value
            if maximum_values:
                maximum_value = max(maximum_value, maximum_values[0][1])
                
            maximum_values.appendleft((start, maximum_value))

        # For each event
        maximum_sum = 0
        for _, end, value in events:
            # Binary search the index of when events no longer overlap
            i = bisect_right(maximum_values, end, key=lambda value: value[0])

            # Compute the maximum sum of non-overlapping events
            if i < n:
                maximum_sum = max(value + maximum_values[i][1], maximum_sum)
            # Or, with this singular event, if no non-overlapping events exist
            else:
                maximum_sum = max(value, maximum_sum)
        
        # Finally, return the maximum sum of non-overlapping events
        return maximum_sum