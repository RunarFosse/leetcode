# Author: Runar Fosse
# Time complexity: O(log n)
# Space complexity: O(1)

class Solution:
    def countCommas(self, n: int) -> int:
        # Iterate over every power of 1000
        commas, current = 0, 1000
        while n > current - 1:
            # While our number is larger, count all commas in its range
            commas += max(n - (current - 1), 0)
            
            # Updating the current power of 1000
            current *= 1000
        
        # Returning the total number of commas in range
        return commas


# Every number above 999 has a comma between the third and fourth digit.
# Every number above 999,999 has another comma between the sixth and seventh digit.

# This can be generalized to: Every number over 1000^x - 1 has x commas.