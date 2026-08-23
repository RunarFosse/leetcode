# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def sumGame(self, num: str) -> bool:
        # Using deduction
        n = len(num)

        # First, count digit sum and '?'s
        left, right = [0, 0], [0, 0]
        for l, r in zip(islice(num, n // 2), islice(reversed(num), n // 2)):
            if l == "?":
                left[0] += 1
            else:
                left[1] += int(l)
            if r == "?":
                right[0] += 1
            else:
                right[1] += int(r)
        
        # Neutralize any noop '?', those appearing on both sides
        noops = min(left[0], right[0])
        left[0] -= noops
        right[0] -= noops

        # Make the left side have zero '?'s
        if left[0]:
            left, right = right, left
        
        # If the total number of '?'s is odd, Alice wins
        if right[0] % 2:
            return True
        
        # Otherwise, if the left sum can be forced by Bob, he wins
        return left[1] != right[1] + 9 * (right[0] // 2)


# It is easy to see that if Alice has full control over the result, she will always win.
# This happens e.g. when Alice makes the final move. Because Alice starts by default,
# she will then always win if there are an odd number of '?'s in the string.

# This leads to another observation. If every '?' is met by another '?' on the other
# side of the string, each move by Alice can be replicated on the other side by Bob,
# not modifying the total digit sum distance between the side, and basically
# resulting in a noop round.

# Now, assume we have an even amount of '?' and they are located on one side.
# Then we will have a digit sum difference between the sides, where Bob wins if
# the difference can be forced to 0, otherwise Alice wins.

# The only way for Bob to win, is if for every pair of '?' on one side,
# it is met with a side difference of 9. In other words, if left has 0 '?', and
# right has x '?'s, then the left digit sum must exactly 9 * (x / 2) more than
# right sum for Bob to force the win. Otherwise, Alice can input a digit making
# a final difference of 0 out-of-bounds for Bob's last move.