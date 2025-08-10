# Author: Runar Fosse
# Time complexity: O(log n)
# Space complexity: O(1)

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        # First, count the digits of n
        digits = self.countDigits(n)
    
        # Then, compute every possible power of two
        power = 1
        while power < 10e9:
            # If the digits match, n can be shuffled to a power of two
            if self.countDigits(power) == digits:
                return True
            power *= 2
        
        # Otherwise, return False
        return False

    def countDigits(self, i: int) -> List[int]:
        # Count and return the digits of i
        digits = [0] * 10
        while i:
            digits[i % 10] += 1
            i //= 10
        return digits