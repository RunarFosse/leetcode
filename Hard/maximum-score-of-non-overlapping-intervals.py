# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        # Using dynamic programming
        self.n = len(intervals)

        # Sort the intervals in ascending order of start, with appended original index
        self.intervals = sorted([(*interval, i) for i, interval in enumerate(intervals)])

        # Then, find and return the maximum score indices of 4 non-overlapping intervals
        return self.opt(0, 4)[1]

    @functools.cache
    def opt(self, i: int, k: int) -> Tuple[int, List[int]]:
        # Base cases
        if k == 0 or i == self.n:
            return (0, [])
        
        # Compute the score when not picking this interval
        skip = self.opt(i + 1, k)

        # Or when picking this interval
        _, end, weight, index = self.intervals[i]
        j = bisect_left(self.intervals, end + 1, key=lambda e: e[0], lo=i)
        score, indices = self.opt(j, k - 1)
        pick = (score + weight, sorted(indices + [index]))

        # Otherwise, return the one with maximal score
        if skip[0] > pick[0]:
            return skip

        # If they have the same score, return the lexicograhically smallest
        if skip[0] == pick[0] and skip[1] < pick[1]:
            return skip
        return pick


# opt(i, k) - The maximum score and indices of k non-overlapping intervals
#             starting at index i (of intervals sorted based on ascending start).

# Base case:
# opt(i, 0) = (0, [])
# opt(n, _) = (0, [])

# Recurrency:
# opt(i, k) = if pick[0] > skip[0] then pick else skip
#           where (score, indices) = opt(j, k - 1)
#                 j = next(j for j in range(i + 1, n) if start[j] > end[i])
#                 pick = (score + weight[i], indices + [index[i]])
#                 skip = opt(i + 1, k)

# No. states = n * 4
# Time complexity per state -> O(log n)
# Total time complexity => O(nlog n)