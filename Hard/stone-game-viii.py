# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        # Using dynamic programming
        n, prefixes = len(stones), list(accumulate(stones))
        
        # Set the initial value of the dp array
        opt = [0] * n
        opt[n - 1] = prefixes[n - 1]

        # And iterate every other index
        for i in reversed(range(n - 1)):
            # Compute current score by picking this index
            pick = prefixes[i] - opt[i + 1]

            # Or skipping, choosing to pick up more stones
            skip = opt[i + 1]

            # Setting the one giving the maximum score difference
            opt[i] = max(pick, skip)

        # Finally, return the maximum score difference Alice can achieve doing moves
        return opt[1]


# opt(i) - The maximum score difference the current player can get by choosing stones
#          starting from index i.

# Base case:
# opt(n - 1) = sum(stones[:n])

# Recurrency:
# opt(i) = sum(stones[:i]) + max(sum(stones[i:j]) - opt(j) for j in range(i + 1, n))

# No. states = n
# Time complexity per state -> O(n)
# Total time complexity => O(n^2)

# By using prefix sums, we can reduce the per state time complexity to O(1),
# through the recurrency:
# opt(i) = max(prefixes[i] - opt(i + 1), opt(i + 1))
# where we either choose to pick this amount of stones, or continue
# picking yet another stone. Because we can pick as many stones as we want, this works!

# Because Alice also has to pick at least 2 stones every turn, our optimal solution
# is stored in opt(1) (and not in the usual opt(0)).