# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # Weighted interval scheduling

        # First we sort all intervals based on their start time
        indices, _ = list(zip(*sorted(enumerate(startTime), key=lambda i : i[1])))
        self.starts = [startTime[i] for i in indices]
        self.ends = [endTime[i] for i in indices]
        self.profits = [profit[i] for i in indices]
        self.n = len(indices)
        
        # Then we do dynamic programming
        return self.opt(0)
    
    @functools.cache
    def opt(self, i: int) -> int:
        # Base case:
        if i == self.n:
            return 0
        
        # Recurrency:
        i_next = bisect_left(self.starts, self.ends[i], lo=i+1)
        take = self.profits[i] + self.opt(i_next)
        skip = self.opt(i+1)

        return max(take, skip)


# This is just weighted interval scheduling, which is solved 
# optimally using dynamic programming.

# opt(i) - Maximum possible profit for jobs after index i.

# Base case:
# opt(n) = 0

# Recurrency;
# opt(i) = max(
#         profit_i + opt(i_next),
#         opt(i+1)
#)
        
# We know that if we "take" the current job, the next valid index (i_next) will
# be sometime in the future, but we are not quite sure when. Instead of iterating
# all values, we can instead binary search to find our index!
        
# n.o. states = n, runtime per state O(log n) (binary searching).
# This gives dp runtime of O(nlog n). Our sorting at the start is also O(nlog n).