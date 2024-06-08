# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # Using prefix sum
        n = len(nums)
        
        # Calculate prefix sum of remainders of array, storing 
        # previously seen prefixes in a set
        prefixes, seen = [0], set()
        for i in range(1, n+1):
            prefixes.append((nums[i-1] + prefixes[i-1]) % k)
            if i >= 2:
                seen.add(prefixes[i-2])
            
            # If we've seen modulo before, then it indicates that
            # the sum of values between is a multiple of k!
            # (as (sum of values between % k) == 0)
            if prefixes[i] in seen:
                return True

        # If we don't, there is no good subarray
        return False