# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    mod = int(1e9 + 7)
    def concatenatedBinary(self, n: int) -> int:
        # Iterate every number
        binary = 0
        for num in range(1, n + 1):
            # Move the current binary number left to make space
            binary = (binary << num.bit_length()) % self.mod

            # And add the new number
            binary = (binary + num) % self.mod
        
        # Finally, return the resulting number
        return binary
