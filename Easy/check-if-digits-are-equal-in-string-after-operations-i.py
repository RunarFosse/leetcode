# Author: Runar Fosse
# Time complexity: O(n^2)
# Space complexity: O(n)

class Solution:
    def hasSameDigits(self, s: str) -> bool:
        # Using simulation
        n = len(s)

        # Turn the string into an array of digits
        digits = [int(c) for c in s]

        # Iteratively operate on pairs of digits, until we are left with two
        for _ in range(2, n):
            for i in range(n - 1):
                digits[i] = (digits[i] + digits[i + 1]) % 10
        
        # Finally, return if the two remaining digits are equal
        return digits[0] == digits[1]
        