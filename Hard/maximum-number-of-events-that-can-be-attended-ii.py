# Author: Runar Fosse
# Time complexity: O(n(k + log n))
# Space complexity: O(nk)

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        # Using dynamic programming
        self.events, self.n = events, len(events)

        # Sort events by ascending start day
        self.events.sort()

        # And precompute next available event after attending another
        starts, self.nexts = [start for start, _, _ in self.events], [0] * self.n
        for i in range(self.n):
            self.nexts[i] = bisect_right(starts, self.events[i][1])

        # And finally, return maximum value from events that can be attended
        return self.opt(0, k)
    
    @functools.cache
    def opt(self, i: int, k: int) -> int:
        # Base cases
        if k == 0 or i == self.n:
            return 0

        # Extract information about this event
        start, end, value = self.events[i]
        
        # And either pick or skip this event
        pick = value + self.opt(self.nexts[i], k - 1)
        skip = self.opt(i + 1, k)

        # And return the maximum valued choice
        return max(pick, skip)

# opt(i, k) - Maximum number of events that can be attended after event i,
#             with k remaining events to be attended

# Base case:
# opt(i, 0) = 0
# opt(n, k) = 0

# Recurrency:
# opt(i, k) = max(opt(i + 1, k), 
#                 value[i] + opt(j, k - 1) where j is first event after i ends)


# No. states = nk
# Time complexity per state = O(1)
# Total time complexity -> O(nk)

# Remember that sorting and precomputing next available event takes O(nlog n) time!