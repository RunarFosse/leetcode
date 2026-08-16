# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        # Iterate the stones
        remainders = [0] * 3
        for stone in stones:
            # Count the occurence of each remainder modulo 3
            remainders[stone % 3] += 1
        zeros, ones, twos = remainders
        
        # If there is an even amount of remainder 0s
        if not zeros % 2:
            # Then Alice wins with at least a remainder 1 and a remainder 2
            return ones > 0 and twos > 0
        
        # Otherwise, Alice requires a stone with a surplus of at least 3
        return abs(ones - twos) > 2


# Because we need to avoid getting a cumulative sum removed that is divisibly by 3,
# we actually only need to focus on the parity of the stones when divided by 3.
# This parity is, of course, when talking in mod 3.

# To prevent instantly losing, Alice needs to pick a stone of remainder 1 or 2.
# The next turn, Bob picks either the same parity stone, respective to which Alice
# took, or a stone with parity 0.

# A parity 0 stone is functionally a no-op stone, swapping the turns without adding
# any to the sum. However, Alice cannot start with such a stone, as this leaves
# the cumulative sum of stones removed to be divided by 3.

# If there are an even amount of these parity 0 stones, Alice can just pass the round
# back to Bob again, acting like nothing happened. Thus, the only special case is
# when the parity 0 stones occur an odd amount of times.

# For the normal case, when we have an even amount of parity 0s. If there only is
# parity 1s, Alice picks one, then Bob picks one, then Alice picks one, and loses.
# Same for parity 2s, where Alice also loses round 3. Only by having both parity 1 and 2s
# can Alice pick the opposite of Bob, until Bob is forced to pick a stone resulting in
# a cumulative removed sum that can be divided by 3.

# For the other case, when we have an odd amount of party 1s, it swaps around.
# Here, Alice needs to be able to counter Bob's moves, even though he can pick
# a parity 0 stone to "turn the tables". Additionally, she needs enough stones
# to force Bob into taking a losing move, as just "using up the stones" leads to Bob win.

# This happens when either parity stone occurs at least three more times than the other.
# For the case of either the same or one more occurence, Bob's parity 0 move forces
# our loss. For two more, Alice "counters" Bob parity 0 move, but it doesn't force him
# into a loss. For three or more, Alice will force Bob to in the end pick a stone
# leading to the cumulative removed sum being divisible by 3, and ending in her win!