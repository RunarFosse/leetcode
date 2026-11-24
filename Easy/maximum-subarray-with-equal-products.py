# Author: Runar Fosse
# Time complexity: O(nlog m)
# Space complexity: O(1)

# where m is the largest possible subarray product.

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        # Using sliding window
        n = len(nums)

        # Slide a window over the array
        maximum = 2
        start, product = 0, 1
        for end in range(n):
            # If the window ever becomes non-coprime
            while gcd(product, nums[end]) != 1:
                # Shrink it
                product //= nums[start]
                start += 1
            
            # Expand the window
            product *= nums[end]
            
            # And store the maximum subarray that is coprime
            maximum = max(end - start + 1, maximum)
        
        # Returning this maximum subarray with equal products
        return maximum


# Two observations.

# 1. For every subarray of size 2, we have that the equivalence holds.
# This comes straight out of the definition for the lowest common multiple:
# lcm(a, b) = |a * b| / gcd(a, b) -> |a * b| = lcm(a, b) * gcd(a, b)
# (this as long as both a and b are positive, which we are guaranteed here)

# 2. For every subarray bigger than 2, the equivalence the whole subarray is coprime!
# If that is the case, then gcd(arr) = 1, and lcm(arr) = prod(arr),
# -> prod(arr) = 1 * lcm(arr).

# We can therefore find the solution to this using sliding window. Expanding window,
# and shrinking it if elements ever become non-coprime!