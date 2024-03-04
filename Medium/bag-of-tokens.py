# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        # Using greedy

        # First sort tokens in ascending order
        tokens.sort()

        # Then play the game using our greedy strategy
        low, high = 0, len(tokens)-1
        score, max_score = 0, 0
        while low <= high:
            # Play lowest face-up
            if tokens[low] <= power:
                score += 1
                max_score = max(score, max_score)
                power -= tokens[low]
                low += 1
            # Play highest face-down
            elif score > 0:
                score -= 1
                power += tokens[high]
                high -= 1
            # Cannot play any more
            else:
                return max_score

        # Return the highest score reached
        return max_score

        
# Greedy strategy:
# Always play the next lowest token face-up until we can't. Then play
# the next highest token face-down until we can play another token face-up.
# We continue until we have no moves left, storing maximum value intermittently.