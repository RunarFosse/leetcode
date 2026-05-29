# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def minElement(self, nums: List[int]) -> int:
        # Iterate the numbers
        minimum = 1e9
        for num in nums:
            # Sum the digits in the number
            digits = 0
            while num:
                digits += num % 10
                num //= 10
            
            # And store the minimum digit sum
            minimum = min(digits, minimum)
        
        # Finally, return this minimum digit sum
        return minimum
