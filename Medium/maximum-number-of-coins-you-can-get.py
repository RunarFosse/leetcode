# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        # Using greedy
        n = len(piles)
        piles.sort()

        coins = 0
        for i in range(n//3):
            coins += piles[n - 2*(i+1)]
        
        return coins
        

# One can maximize the amount of coins you get by at each step, choosing
# the three piles with most coins, second most coins and least most coins in total.
# You cannot change what Alice will pick, however you can always minimize the amount Bob
# is picking. 