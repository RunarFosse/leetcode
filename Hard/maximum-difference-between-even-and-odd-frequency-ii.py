# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        # Using prefix sum
        n = len(s)

        # Iterate over every valid character pair
        maximum = -1e9
        for a in "01234":
            for b in "01234":
                # The same character would give a constant zero difference
                if a == b:
                    continue

                # Store prefix counts of the different characters
                a_start, a_end = 0, 0
                b_start, b_end = 0, 0

                # As well as the smallest difference per count parity
                differences = [[1e9, 1e9], [1e9, 1e9]]

                # Through sliding a window over the string
                start = 0
                for end in range(n):
                    # Incrementing current character counts
                    if s[end] == a:
                        a_end += 1
                    elif s[end] == b:
                        b_end += 1
                    
                    # While the window is sized at least k, and possibly a having 
                    # non-zero even count of character b
                    while end - start + 1 >= k and b_end - b_start > 1:
                        # Compute the parity of the different prefix counts
                        a_parity, b_parity = a_start % 2, b_start % 2

                        # And store the current smallest difference between these counts
                        difference = a_start - b_start
                        current = differences[a_parity][b_parity]
                        differences[a_parity][b_parity] = min(difference, current)

                        # Then shrink the window
                        if s[start] == a:
                            a_start += 1
                        elif s[start] == b:
                            b_start += 1
                        start += 1
                    
                    # Now, find best window where a is odd, b is even,
                    # and the previous k size and non-zero b requirement is upheld too
                    a_parity, b_parity = a_end % 2, b_end % 2
                    smallest = differences[a_parity ^ 1][b_parity]
                    if smallest < 1e9:
                        maximum = max(a_end - b_end - smallest, maximum)

        # Finally, return this maximum difference between any two characters in that subs
        return maximum


# The major observation simplifying computation is that by maximizing the difference
# between any two character counts a and b, i.e. maximizing (a_count - b_count).

# By utiziling prefix sums we have this equation to be maximized:
# (a_end - a_start) - (b_end - b_start).

# This can be reordered into the equation:
# (a_end - b_end) - (a_start - b_start)

# This is even simpler to compute using a two pointer approach.