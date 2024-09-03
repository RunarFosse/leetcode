# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        # First turn the string into a number
        number = 0
        for c in s:
            # Replace character with position
            position = ord(c) - ord("a") + 1

            # Concatenate with number
            number *= 10 if position < 10 else 100
            number += position
        
        # Then transform the number at most k times
        for _ in range(k):
            # Early escape if digitsum stays the same
            if number < 10:
                break

            # Sum over the digits
            digitsum = 0
            while number:
                digitsum += number % 10
                number //= 10
            number = digitsum

        # Return transformed number
        return number