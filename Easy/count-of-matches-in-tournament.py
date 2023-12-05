# Author: Runar Fosse
# Time complexity: O(1)
# Space complexity: O(1)

class Solution:
    def numberOfMatches(self, n: int) -> int:
        return n - 1
        

# We could do the iterative, recursive version.
# However, logically, we know that every match the losing team gets eliminated.
# How many teams need to be eliminated from n before n == 1? Obviously n - 1.
# Therefore, a total of n - 1 matches will be played.