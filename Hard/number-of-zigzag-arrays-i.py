# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(m)

class Solution:
    mod = int(1e9 + 7)
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        # Using dynamic programming

        # First, compute the number of valid values on the range [l, r]
        m = r - l + 1

        # Then, iterate every array range, utilising slope symmetry for array
        opt = [1] * m
        for _ in range(n - 1):
            # Compute prefix sum and store in-place
            prefix = 0
            for j in range(m):
                opt[j], prefix = prefix, (prefix + opt[j]) % self.mod
            
            # And reverse to ensure the correct mirrored slope order
            opt.reverse()

        # Finally, return the number of valid ZigZag arrays
        return 2 * sum(opt) % self.mod


# opt(i, end, slope) - The number of valid ZigZag arrays of length i, ending on a given
#                      value end, and where the two last elements are either 
#                      strictly increasing (slope=1), decreasing (slope=-1).

# Base case:
# opt(1, end, _) = 1 if end in [l, r] else 0

# Recurrency:
# opt(i, end, slope) = sum(opt(i - 1, next, sign(end - next)) for next in nexts)
#                    where nexts | slope > 0 = [l, end)
#                                | slope < 0 = (end, r]

# By using prefix sums we can optimize calculation per state from O(m) to O(1),
# As sum(opt(i - 1, next, sign(end - next)) for next in nexts) is equal to:
#    slope > 0 | prefix_opt(i - 1, end - 1, -1)
#    slope < 0 | prefix_opt(i - 1, r, 1) - prefix_opt(i - 1, end, 1)

# Another observation: The arrays of slope < 0 and slope > 0 are mirror images of
# eachother! This reduces space even further by allowing us to utilize only 1 array.

# We use the previous' iterations values so can optimize space over n iterations:
# No. iterations = n
# No. states = m * 2
# Time complexity per state -> O(1)

# Total time complexity => O(mn)
# Total space complexity => O(m)