# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        # Using sliding window
        n = len(nums)

        start, minLength = 0, 1e9
        window, bits = 0, [0] * 30
        for i in range(n):
            # Extend the window
            window |= nums[i]

            # And increment set bits
            for j in range(30):
                bits[j] += (nums[i] >> j) & 1
            
            # If window is bigger than k, shrink it
            while start <= i and window >= k:
                # First store subarray length
                minLength = min(i - start + 1, minLength)

                # Remove set bits from window count
                for j in range(30):
                    if (nums[start] >> j) & 1:
                        bits[j] -= 1
                        if not bits[j]:
                            window -= (1 << j)
                
                # Move the pointer
                start += 1
            
        # Finally return the minimum subarray length
        return minLength if minLength < 1e9 else -1


# We have that k is upper bounded by 10^9, which again is upper bounded
# by 30 bits. Therefore we can represent the window as a 30 sized array,
# containing the frequency of each set bit in the current window.

# Iterating over this fixed size bit array is also O(1).