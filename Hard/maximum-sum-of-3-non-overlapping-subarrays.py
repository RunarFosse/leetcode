# Author: Runar Fosse
# Time complexity: O(nk)
# Space complexity: O(nk)

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        # Using dynamic programming
        self.k = k

        # First compute the sum of all subarrays
        self.subarrays = []
        window, window_sum = deque([]), 0
        for num in nums:
            window.append(num)
            window_sum += num

            if len(window) == k:
                self.subarrays.append(window_sum)
                window_sum -= window.popleft()
        
        # Then compute the maximum sum of 3 non-overlapping subarrays
        _, indices = self.opt(0, 3)
        return indices

    @functools.cache
    def opt(self, i: int, remaining: int) -> (int, List[int]):
        if remaining == 0 or i >= len(self.subarrays):
            return (0, [])

        # Compute pick and skip sums
        pick = self.opt(i + self.k, remaining - 1)
        pick = (pick[0] + self.subarrays[i], [i] + pick[1])

        skip = self.opt(i + 1, remaining)

        # Return the largest, lexicographically smallest
        return pick if pick[0] >= skip[0] else skip

# Number of states => n * k
# Runtime per state =>  O(1)