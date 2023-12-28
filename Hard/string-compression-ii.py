# Author: Runar Fosse
# Time complexity: O(n^2*k)
# Space complexity: O(m*n)

class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        # Using dynamic programming
        self.s = s
        return self.opt(0, k, ("", None))

    @functools.cache
    def opt(self, i: int, k: int, last: Tuple[str, int]) -> int:
        n = len(self.s)
        # Base cases
        if i == n:
            return 0 if k == 0 else 1e9

        # Recurrency
        c, m = self.s[i], 0
        # Calculate homogeneous sequence length
        while i+m < n and self.s[i+m] == c:
            m += 1

        opt = 1e9
        for removes in range(min(k+1, m+1)):
            current = 0
            # If not removing whole sequence
            if removes < m:
                remaining = m - removes
                if last[0] == c:
                    remaining += last[1]
                    current -= self.compress(last[1])
                current += self.compress(remaining)
                current += self.opt(i + m, k - removes, (c, remaining))
            # Else if removing whole sequence
            else:
                current += self.opt(i + m, k - removes, last)

            # Keep minimum of the options
            opt = min(current, opt)

        return opt

    def compress(self, m: int) -> int:
        # Compression function for a homogenous sequence of length m
        if m < 10:
            return min(m, 2)
        
        return 3 if m < 100 else 4


# opt(i, k, (c, m_last)) - Optimal compression length for s[i:] given k deletions
# and with the previous non-zero-length remaining homogenous behind this current 
# sequuence consisting of character c and being of length m_last.

# Base case:
# opt(i, 0, _) = Compression length of s[i:]
# opt(n, k, _) = 0 if k == 0 else Infinity

# Recurrency;
# opt(i, k, (c, m_last)) = min(
#      (opt(i+m, k-m') + compress_len of s[i+m':i+m]) for m' in [0..min(k, m-1)]
#      + opt(i+m, k-m) + 0 if last sequence and next sequence contain the same
#      character, else the combined compression length of both - compression length of last)
# given that s[i] is the start of a homogeneous sequence of length m.

# Note, we need a seperate check for when m' == m, as this might "merge" two different
# homogeneous sequences.


# N.o. states = n*k, runtime per state = m. Giving runtime => O(mnk).
# However, m is homogeneous subsequence length, upper bounded by n.
# Thus, final time complexity => O(n^2*k).