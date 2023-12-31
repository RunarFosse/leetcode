# Author: Runar Fosse
# Time complexity: O(log n)
# Space complexity: O(1)

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Using two pointer approach
        if x <= 0:
            return False if x < 0 else True
        
        low, high = 0, floor(log10(x))
        while low <= high:
            # Find each digit at position low and high
            dlow = (x % pow(10, low+1) - x % pow(10, low)) // pow(10, low)
            dhigh = (x % pow(10, high+1) - x % pow(10, high)) // pow(10, high)

            # Check if they are unequal
            if dlow != dhigh:
                return False

            # Continue iterating
            low += 1
            high -= 1
        
        return True

# Time complexity is given with respect to number x.
# As runtime grows linearly with the length of x (as a string),
# it grows logarithmically with the magnitude of x (as a number).