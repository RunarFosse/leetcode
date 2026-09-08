# Author: Runar Fosse
# Time complexity: O(1)
# Space complexity: O(1)

class Solution:
    def countCommas(self, n: int) -> int:
        # Count the total number of commas in our range
        return max(n - 999, 0)


# Because n is at most 10^5 = 10,000,
# then each number can at most contain 1 comma.

# That also means the first 999 numbers contain no commas,
# while the rest of the numbers contain exactly one comma.
# Thus, the number of commas for an n >= 1000 is n - 999.