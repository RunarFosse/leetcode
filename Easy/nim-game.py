# Author: Runar Fosse
# Time complexity: O(1)
# Space complexity: O(1)

class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4

# You win:  1 - 2 - 3 - 5 - 6 - 7 - 9 - 10 - 11
# You lose: 4 - 8 - 12

# From this we can extrapolate that we lose only if the number of stones at
# the start is a multiple of 4. We win any other time.