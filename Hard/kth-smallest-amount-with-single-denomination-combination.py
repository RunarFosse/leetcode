# Author: Runar Fosse
# Time complexity: O(2^nlog k)
# Space complexity: O(2^n)

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        # Using binary search

        # First, remove any coin that is a multiple of another
        coprimes = []
        for coin in sorted(coins):
            if all(coin % other for other in coprimes):
                coprimes.append(coin)
        self.coins = coprimes
        n = len(coprimes)

        # And binary search the k'th smallest amount combination
        left, right = 0, self.coins[0] * k + 1
        while left < right:
            pivot = (left + right) // 2

            # By computing how many unique combinations of coins we can create
            count = 0
            for mask in range(1, 1 << n):
                # That result in an amount less than pivot
                if self.lcm(mask) > pivot:
                    continue
                
                # Using inclusion-exclusion principle to compute count
                if mask.bit_count() % 2:
                    count += pivot // self.lcm(mask)
                else:
                    count -= pivot // self.lcm(mask)
            
            # And move boundaries accordingly
            if count >= k:
                right = pivot
            else:
                left = pivot + 1
                
        # Finally, return this k'th smallest amount
        return left

    @functools.cache
    def lcm(self, mask: int) -> int:
        # Compute the lowest common multiple of coins within a bitmask,
        # using the iterative reduction formula
        if mask == 0:
            return 1

        # First, remove a specific coin index
        other = mask & (mask - 1)
        index = (mask ^ other).bit_length() - 1
        coin = self.coins[index]

        # And compute the iterative reduction lcm
        reduced = self.lcm(other)
        return reduced // gcd(reduced, coin) * coin
