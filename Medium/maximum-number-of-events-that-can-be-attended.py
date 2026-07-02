# Author: Runar Fosse
# Time complexity: O((m + n)log n)
# Space complexity; O(n)

# where m is the total number of days

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        # Using greedy
        n = len(events)

        # First, sort the events in ascending order of start day
        events.sort()

        # Then, iterate every event
        attended, day = 0, 1
        i, queue = 0, []
        while i < n or queue:
            # Add (the end day of) all the events happening today to the heap
            while i < n and events[i][0] <= day:
                heappush(queue, events[i][1])
                i += 1
            
            # Then, remove any event that has already finished
            while queue and queue[0] < day:
                heappop(queue)
            
            # If we have a valid event to attend, do so
            if queue:
                heappop(queue)
                attended += 1
            
            # And increment the day
            day += 1
        
        # Finally, return number of attended events
        return attended
