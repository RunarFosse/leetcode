# Author: Runar Fosse
# Time complexity: O(log n)
# Space complexity: O(1)

class Solution:
    def findComplement(self, num: int) -> int:
        result = 0

        # Iterate every bit in num
        i = 0
        while num >> i:
            # Calculate the current bit complement
            complement = 1 ^ (num >> i & 1)

            # And add it to result
            result += complement << i
            i += 1

        return result