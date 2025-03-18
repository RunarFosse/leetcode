# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        # Using sliding window
        n = len(nums)

        # Move a sliding window
        start, current, longest = 0, 0, 0
        for i in range(n):
            # While AND over current subarray OR sum is 1
            while nums[i] & current:
                # Slide window by removing bits from starting element
                current ^= nums[start]
                start += 1

            # Store the current nice subarray size
            longest = max(i - start + 1, longest)

            # And add to current OR sum
            current |= nums[i]

        # Return the longest nice subarray
        return longest