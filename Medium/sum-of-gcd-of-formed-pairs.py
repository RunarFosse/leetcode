# Author: Runar Fosse
# Time complexity: O(n(log n + log m))
# Space complexity: O(n)

# where m is the maximum value of the array

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        # Using two pointer
        n = len(nums)

        # First, extract the running maximum value and compute the prefix GCD
        maximum = 0
        for i in range(n):
            maximum = max(nums[i], maximum)
            nums[i] = self.gcd(nums[i], maximum)
        
        # Sort the resulting numbers in ascending order
        nums.sort()

        # Then, form and sum over the GCD of all formed pairs
        total = 0
        for i in range(n // 2):
            total += self.gcd(nums[i], nums[n - i - 1])
        
        # Finally, return this sum
        return total
    
    def gcd(self, a: int, b: int) -> int:
        # Compute the GCD between two numbers
        while b != 0:
            a, b = b, a % b
        return a
