# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        # Using dynamic programming
        n = len(arr)

        # First, initialize the dynamic programming array
        opt = [inf] * (n + 1)

        # Then, iterate every start index
        smallest = inf
        current, end = 0, n
        for start in reversed(range(n)):
            # Expand the window
            current += arr[start]

            # And shrink it until we are at or below the target
            while current > target:
                end -= 1
                current -= arr[end]

            # Temporarily carry the next index's result
            opt[start] = opt[start + 1]
            
            # If our current window sums to target
            if current == target:
                # Store the minimum subarray size
                size = end - start
                opt[start] = min(size, opt[start])

                # Also storing length of smallest two non-overlapping subarrays
                smallest = min(size + opt[end], smallest)
        
        # If there is no such smallest two non-overlapping subarrays with target sum
        if smallest == inf:
            # Then return -1
            return -1
        
        # Otherwise, return the combined length of these two smallest subarrays
        return smallest


# opt(i) - The length of the smallest subarray after index i that sums to target.

# Base case:
# opt(n) = inf

# Recurrency:
# opt(i) | end is None = opt(i + 1) 
#        | otherwise = min(end - i + 1, opt(end))
#        where end = next(j for j in range(i + 1, n) if sum(arr[i:j]) == target)

# No. states = n
# Time complexity per state -> O(n)
# Total time complexity => O(n^2)

# By using an iterative sliding-window approach, we can reduce the time complexity
# per state to O(1), resulting in a total time complexity of O(n).