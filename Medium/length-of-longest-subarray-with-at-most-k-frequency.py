# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        # Using sliding window
        n = len(nums)

        p1, p2 = 0, 0
        frequencies = defaultdict(int)
        max_subarray = 0
        while p2 < n:
            # Expand the window
            frequencies[nums[p2]] += 1

            # While the window does not fit the constraints, shrink it
            while p1 < p2 and frequencies[nums[p2]] > k:
                frequencies[nums[p1]] -= 1
                p1 += 1
            
            # Store the maximum size of any subarray
            p2 += 1
            max_subarray = max(p2 - p1, max_subarray)

        return max_subarray