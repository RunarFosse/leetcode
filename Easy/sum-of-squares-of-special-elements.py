# Author: Runar Fosse
# Time complexity: O(sqrt(n))
# Space complexity: O(1)

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        # Iterate every index up to the root of the array length
        total, i, n = 0, 1, len(nums)
        while i * i <= n:
            # If the current index divides n
            if n % i == 0:
                # We have found two special elements, so add their squares to total
                total += nums[i - 1] * nums[i - 1]
                if i * i < n:
                    # If the index is the square root, then i == (n / i), only count once
                    total += nums[n // i - 1] * nums[n // i - 1]
            i += 1

        # And return the sum of squares of all special elements
        return total


# An element is special if its index divides the length of the array. 
# If a given index i divides n, then there must exist a corresponding (n / i) which
# also divides n (as i * (n / i) == n). This optimizes time complexity significantly.