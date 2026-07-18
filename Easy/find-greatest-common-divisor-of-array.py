# Author: Runar Fosse
# Time complexity: O(n + log m)
# Space complexity: O(1)

# where m is the maximum element in the array

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        # Using Euclidean algorithm

        # First, find the minimum and maximum element in the array
        minimum, maximum = inf, 0
        for num in nums:
            minimum = min(num, minimum)
            maximum = max(num, maximum)
        
        # And return their greatest common divisor
        return self.gcd(minimum, maximum)
        
    def gcd(self, a: int, b: int) -> int:
        # Find the greatest common divisor between a and b
        while b != 0:
            # Using the Euclidean algorithm to iteratively reduce the remainder to zero
            a, b = b, a % b
        
        # The resulting quotient is our GCD
        return a
