# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        # Using prefix sum
        n = len(nums)

        # Keep a running prefix sum of the array
        prefix, prefixes = 0, {0: 0}
        maximum = None
        for i in range(n):
            prefix += nums[i]

            # Compute the remainder of the next index divided by k
            remainder = (i + 1) % k

            # If we have seen this remainder before
            if remainder in prefixes:
                # Store the current largest subarray with a length divisible by k
                subarray = prefix - prefixes[remainder]
                if maximum is None or subarray > maximum:
                    maximum = subarray

            # And then store the smallest prefix at this current remainder
            if remainder not in prefixes or prefix < prefixes[remainder]:
                prefixes[remainder] = prefix
        
        # Finally, return the maximum subarray with a length divisible by k
        return maximum
