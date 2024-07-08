# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # Using iterative approach

        # Solve for the winner using governing equation
        starter = 0
        for players in range(1, n+1):
            starter = (starter + k) % players

        # Return starter+1 (as starter is 0-indexed while winner is 1-indexed)
        return starter+1
        
# For any given game n,k it is obvious that the winner is equal to
# (((...k%1 + ...)% (n-2) + k) % (n-1) + k) % n

# This is because the next starting player round 1 is governed by the equation
# k % n
# For round 2 it is governed by
# (k % (n-1) + k % n) % n = (k % (n-1) + k) % n
# This goes on until there is only 1 person left, i.e. % 1.
# Luckily, the person starting when only 1 person is left is the winner!