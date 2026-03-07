# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def minFlips(self, s: str) -> int:
        # Using sliding window
        n = len(s)

        # First, iterate the string
        pattern1, pattern2 = 0, 0
        for i in range(n):
            # Count the flips per pattern without any string rotations
            if i % 2 == 0:
                if s[i] == "0":
                    pattern2 += 1
                else:
                    pattern1 += 1
            else:
                if s[i] == "0":
                    pattern1 += 1
                else:
                    pattern2 += 1

        # Compute the minimum bit flips per pattern
        minimum = min(pattern1, pattern2)

        # If the string has even length, return early
        if n % 2 == 0:
            return minimum
        
        # Otherwise, iterate all possible other rotations
        for i in range(n - 1):
            # And simulating rotations
            if s[i] == "0":
                pattern1 += 1
                pattern2 -= 1
            else:
                pattern1 -= 1
                pattern2 += 1
            pattern1, pattern2 = pattern2, pattern1
            
            # Then store the minimum flips per pattern after rotation
            minimum = min(pattern1, pattern2, minimum)
        
        # Finally, return the minimum bit flips to make binary string alternating
        return minimum



# 1101011
# 
# 0101010 - 2
# 1010101 - 5

# 101011        -   1010111
# 
# 010101 - 5    -   0101010 - 6
# 101010 - 1    -   1010101 - 1

# 01011         -   010111          -   0101111
# 
# 01010 - 1     -   010101 - 1      -   0101010 - 2
# 10101 - 4     -   101010 - 5      -   1010101 - 5

# Keep two counters. One for bit flips for pattern 1, and one for pattern 2.
# When shrinking the window, decrement the counter for pattern where removed bit
# does not match, and swap the counters.
# When expanding the window, increment the counter for pattern where added bit
# does not match.

# These two operations can be coalesced into:
# Decrement the counter for pattern where removed bit does not match.
# Then increment the counter for pattern where the removed bit does match.
# Then swap the counters.
# Although less intuitive, it makes for cleaner code.

# This can trivially be even further reduced down to a increment/decrement
# only if the string has an odd length, per bit.
# Meaning that we can return early if the string is of odd length.