# Author: Runar Fosse
# Time complexity: O(mlog k)
# Space complexity: O(1)

# where k is the maximum quantity of a given product

class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        # Using binary search
        self.n, self.quantities = n, quantities

        # Binary search the maximum amount to distribute
        lo, hi = 1, max(quantities)
        while lo < hi:
            x = (lo + hi) // 2

            if self.isDistributable(x):
                hi = x
            else:
                lo = x+1
        
        # Return the minimized maximum amount
        return lo

    def isDistributable(self, x: int) -> bool:
        # Verify that we can distribute to all store,
        # given at most x products to each
        stores = 0
        for quantity in self.quantities:
            stores += ceil(quantity / x)
        
        return stores <= self.n