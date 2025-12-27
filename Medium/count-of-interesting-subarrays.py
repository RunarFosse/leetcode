# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(min(n, modulo))

class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        # Using prefix sum
        n = len(nums)

        # Keep count of number of seen subarrays indexed by elements with remainder k
        subarrays = defaultdict(int)
        subarrays[0] = 1

        # Iterate the array
        interesting, prefix = 0, 0
        for i in range(n):
            # Keep a running prefix sum of elements with remainder equal to k
            prefix += 1 if nums[i] % modulo == k else 0
            prefix %= modulo

            # Count new interesting subarrays
            interesting += subarrays[(prefix - k + modulo) % modulo]

            # And increment subarray with prefix
            subarrays[prefix] += 1

        # Finally, return the number of interesting subarrays
        return interesting
