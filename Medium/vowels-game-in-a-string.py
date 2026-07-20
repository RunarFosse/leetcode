# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def doesAliceWin(self, s: str) -> bool:
        # Using greedy
        
        # Iterate the string
        for c in s:
            # If we find a vowel, Alice wins
            if c in "aeiou":
                return True
        
        # Otherwise, Bob wins
        return False


# Given the string s contains x vowels.

# If x is odd:
# Alice takes the whole string, and wins.

# If x is even:
# Alice takes the largest odd number smaller than x, leaving 1 vowel left.
# 1 is an odd number, so Bob cannot make a move. Alice wins again.

# However, if there are no vowels, then x is 0.
# If x is 0, Alice cannot make a move. Bob wins.

# Therefore, if there are 0 vowels in s, Bob wins.
# Otherwise, Alice wins.