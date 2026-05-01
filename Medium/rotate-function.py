# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        # Using dynamic programming
        n = len(nums)

        # First, compute the total sum of the array
        total = sum(nums)

        # Then, compute the base case F(0)
        F = 0
        for i in range(1, n):
            F += i * nums[i]
        
        # At last, compute the remaining values of F and store the maximum
        maximum = F
        for i in range(1, n):
            F += total - n * nums[n - i]
            maximum = max(F, maximum)
        
        # Finally, return this maximum value of F
        return maximum


# F(i) - giving the value of the rotate function F(i) directly

# Base case:
# F(0) = 0 * nums[0] + 1 * nums[1] + ... + (n - 1) * nums[n - 1]

# Recurrency:
# F(i) = F(i - 1) + total - n * nums[n - i]
