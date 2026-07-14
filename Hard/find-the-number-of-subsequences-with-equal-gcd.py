# Author: Runar Fosse
# Time complexity: O(nm^2)
# Space complexity: O(m^2)

class Solution:
    mod = int(1e9 + 7)
    def subsequencePairCount(self, nums: List[int]) -> int:
        # Using dynamic programming

        # First, extract the maximum value of nums
        maximum = max(nums)

        # Initialize the array containing number of pairs per gcd pair
        opt = [[0] * (maximum + 1) for _ in range(maximum + 1)]

        # And initialize pair of empty sequences
        opt[0][0] = 1

        # Then, iterate every value in the array
        for num in nums:
            # Keep a temporary copy to avoid overrides
            previous = [row[:] for row in opt]

            # Precompute all gcd values
            gcds = [self.gcd(num, i) for i in range(maximum + 1)]
            
            # Then, iterate every pair of possible existing gcd values
            for j in range(maximum + 1):
                for k in range(maximum + 1):
                    # If there are no subsequence pairs with these gcds
                    pairs = previous[j][k]
                    if pairs == 0:
                        # There are no sequences to add current number to
                        continue
                    
                    # Then add number to either the first or the second sequence
                    opt[gcds[j]][k] = (opt[gcds[j]][k] + pairs) % self.mod
                    opt[j][gcds[k]] = (opt[j][gcds[k]] + pairs) % self.mod
        
        # Then, compute the number of pairs of non-empty sequences with equal gcd
        pairs = 0
        for i in range(1, maximum + 1):
            pairs += opt[i][i]
            pairs %= self.mod

        # And return
        return pairs

    @functools.cache
    def gcd(self, a: int, b: int) -> int:
        # Compute the gcd between two numbers
        while b != 0:
            a, b = b, a % b
        return a


# opt(i, j) - The number of pairs of subsequences with gcd of the first
#             sequence being i, gcd of the second sequence being j.

# No. states = m * m
# Time complexity per state -> O(1)
# No. iterations over each state = n

# Final time complexity => O(nm^2)