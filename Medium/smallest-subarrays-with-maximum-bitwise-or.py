# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        # Using bit manipulation
        n = len(nums)

        # Iterate the array backwards
        subarrays, bits = deque([]), [0] * 32
        for i in reversed(range(n)):
            # For each set bit, store index when last set
            num, bit = nums[i], 0
            while num:
                if num & 1:
                    bits[bit] = i
                num >>= 1
                bit += 1

            # And compute the smallest subarray for OR to be maximized
            length = max(bits) - i + 1
            subarrays.appendleft(max(length, 1))
        
        # Finally, return the lengths of these smallest subarrays
        return list(subarrays)