# Author: Runar Fosse
# Time complexity: O(nsqrt(m))
# Space complexity: O(1)

# where m is the largest number in the array

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        # Compute the four divisors of each element in the array
        divisors = map(self.computeFourDivisors, nums)

        # And return the sum of all
        return sum(divisors)
    
    def computeFourDivisors(self, num: int) -> int:
        # Compute the divisors and their total sum, from a number
        divisors, current, i = 0, 0, 1
        while i*i <= num:
            if not num % i:
                left, right = i, num // i
                divisors += 1
                current += left
                if left != right:
                    divisors += 1
                    current += right

                # If we have more than 4 divisors, return early
                if divisors > 4:
                    return 0
            i += 1
        
        # If we have less than 4 divisors, return 0, otherwise return the sum
        return 0 if divisors < 4 else current
