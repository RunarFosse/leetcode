# Author: Runar Fosse
# Time complexity: O(1)
# Space complexity: O(1)

class Solution:
    def minimumPushes(self, word: str) -> int:
        # Using greedy
        n = len(word)

        # First, compute the number of complete key spot groups
        groups, remainder = divmod(n, 8)

        # And compute the minimum number of pushes
        return groups * (groups + 1) // 2 * 8 + (groups + 1) * remainder

        
# We are guaranteed that the word will only consist of distinct characters.

# Therefore, the number of characters is given by the string length n.

# Greedily assign 8 characters the first key spot, 8 the second, etc.
# This will minimize the number of pushes to type the word.

# Computing the number of full groups + remainder of last group, we have
# the total number of pushes:
# 1 * complete group 1 + 2 * complete group 2 + 3 * complete group 3 + 4 * remainder

# OR
# 1 * complete group 1 + 2 * remainder

# It all depends where the remainder lies.
# This can be simplified to (for the first)
# (1 + 2 + 3) * 8 + 4 * (n - 3 * 8)

# OR
# 1 * 8 + 2 * (n - 8)

# Generalized, we have:
# sum [1..groups] * 8 + (groups + 1) * remain,
# given groups complete groups and remain remaining characters