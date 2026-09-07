# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    mod = int(1e9 + 7)
    def distinctSubseqII(self, s: str) -> int:
        # Using dynamic programming
        opt = [0] * 26

        # Iterate every character in the string
        total, indexOf = 0, lambda c: ord(c) - ord("a")
        for c in s:
            index = indexOf(c)

            # Compute the number of new subsequences at this character
            new = (total + 1) % self.mod

            # Remove duplicates, and add them to the total
            total = (total + new - opt[index]) % self.mod

            # Storing the current "new" subsequences in the dp array
            opt[index] = new

        # Finally, return the number of distinct non-empty subsequences of s
        return total


# We are trying to find the amount of distinct non-empty subsequences of s.
# Given the string "abca":

# Initially, we only have the subsequence "a".
# Then, adding the next character, we can add "b", and append it to all other seen
# subsequences aswell, resulting in a total "a", "b", "ab".
# The same happens for the next one, with "c",
# resulting in "a", "b", "ab", "c", "ac", "bc", "abc".

# Then, we have another "a". Here comes the edge case, we've already added this alone.
# Therefore, we have to add "a" to all previously seen subsequences, then removing
# duplicates. In this example, adding "a" to the end of "a", "b", "ab", "c", "ac", "bc",
# "abc"

# This result in the final amount:
# "a", "b", "ab", "c", "ac", "bc", "abc", "aa", "ba", "aba", "ca", "aca", "bca", "abca".

# Instead of storing the strings directly, we can count the number of distinct non-empty
# subsequences, noting that for a given index i, the number of new subsequences is:
# subsequences[i] = 2 * subsequences[i - 1] + 1
# as we add the current character by itself, and append it to all previously seen!

# For a character seen before at index j, this would then instead become:
# subsequences[i] = 2 * subsequences[i - 1] - subsequences[j - 1]

# Also, instead of storing subsequences directly per index, we can
# store them at each seen character index!

# This runs in O(n) time, with O(1) space!

# Turned into a recurrence relation and proper DP description, we have:

# opt[i](c) - The number of subsequences ending at the character c,
#             iterated over the string until index i.

# Base case:
# opt[0](c) = 0

# Recurrency:
# opt[i](c) = total[i - 1] + 1
#           with total[i] = total[i - 1] + opt[i](c) - opt[i - 1](c)

# No. states = 26
# Time complexity per state -> O(1)
# Total time complexity with bottom-up iteration over all indices => O(n)

# The final result is given by counting up the number of distinct subsequences over
# all indices of the string (ensuring to remove duplicates)!