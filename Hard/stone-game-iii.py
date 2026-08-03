# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        # Using dynamic programming
        n = len(stoneValue)

        # Iterate the stones
        opt = [0] * 3
        for i in reversed(range(n)):
            # Either pick 1, 2 or 3 stones (if we can)
            stones = stoneValue[i]
            score = stoneValue[i] - opt[(i + 1) % 3]
            if i < n - 1:
                stones += stoneValue[i + 1]
                score = max(stones - opt[(i + 2) % 3], score)
            if i < n - 2:
                stones += stoneValue[i + 2]
                score = max(stones - opt[(i + 3) % 3], score)
            opt[i % 3] = score
        
        # Alice starts, if she has a positive point differential, she wins
        if opt[0] > 0:
            return "Alice"
        
        # If the differential is 0, they have the same score, and it is a tie
        if opt[0] == 0:
            return "Tie"

        # Otherwise, Bob wins
        return "Bob"


# opt(i) - The maximum score difference the next player picking can acquire
#          over the other, by picking either 1, 2 or 3 stones from index i and upwards.

# Base case:
# opt(n) = 0

# Recurrency:
# opt(i) = max(
#               stones[i] - opt(i + 1),
#               stones[i] + stones[i + 1] - opt(i + 2),
#               stones[i] + stones[i + 1] + stones[i + 2] - opt(i + 3)
#          )

# No. states = n
# Time complexity per state -> O(1)
# Total time complexity: O(n)

# By using an iterative, bottom-up dynamic programming approach, we can reduce
# the number of states to only 3, holding opt(i + 1), opt(i + 2), opt(i + 3).
# This can easily be stored in a rotating array using modulo 3.
# This in turns reduces space complexity to O(1).