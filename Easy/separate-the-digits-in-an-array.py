# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        # Iterate the numbers from the back
        digits = []
        for num in reversed(nums):
            # Separate the digits in the reversed order
            while num:
                digit = num % 10
                num //= 10
                digits.append(digit)
        
        # Finally, reverse the array to correct order and return
        digits.reverse()
        return digits
