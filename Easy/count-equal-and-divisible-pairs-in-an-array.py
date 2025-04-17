# Author: Runar Fosse
# Time complexity: O(nk)
# Space complexity: O(n)

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        pairs = 0

        # For each index i in the array
        frequencies = defaultdict(lambda: defaultdict(int))
        for i, num in enumerate(nums):
            # For every previous seen number
            for modulo, frequency in frequencies[num].items():
                # Count pair if index product is divisible by k
                if not (i * modulo) % k:
                    pairs += frequency

            # And count the frequency of the current number at i % k
            frequencies[num][i % k] += 1

        return pairs

# (i * j) being divisble by k, is the same as
# (i * j) % k == 0, which again is the same as
# (i % k) * (j % k) % k == 0
# There only exists k values for (j % k),
# which we can use to optimize computation