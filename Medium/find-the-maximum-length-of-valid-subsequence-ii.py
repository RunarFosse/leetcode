# Author: Runar Fosse
# Time complexity: O(nk + k^2)
# Space complexity: O(k^2)

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        # Using dynamic programming
        opt = [[0] * k for _ in range(k)]

        # Iterate the array
        subsequence = 0
        for num in nums:
            # Find the number modulo k
            num %= k

            # For every modulo k
            for modulo in range(k):
                # Add num to the largest subsequence with said modulo
                opt[modulo][num] = opt[num][modulo] + 1
                
                # And store the current largest subsequence
                subsequence = max(opt[modulo][num], subsequence)
        
        # Finally, return said largest subsequence
        return subsequence

# We a constraint that, for a number val < k, in a subsequence:
# (nums[i] + nums[j]) % k == val
#
# This can be rewritten as:
# nums[i] % k == (val - (nums[j] % k)) % k
#
# We can iterate over previous (val - (nums[j] % k)) % k as 'modulo', giving us:
# nums[i] % k == modulo
#
# By iterating over modulo < k we can find all subsequences to add nums[i] to!