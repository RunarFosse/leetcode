# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(1)

class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        # Iterate every query
        operations = 0
        for start, end in queries:
            # Counting the sum of operations to zero the range [start, end]
            current = self.countOperations(end) - self.countOperations(start - 1)

            # Divided by two, as we can perform a division twice per operation
            operations += (current + 1) // 2
        
        # Finally, return the minimum number of total operations
        return operations

    def countOperations(self, n: int) -> int:
        # Count the sum of operations to zero the range [1, n]
        operations = 0

        # In powers of four
        current, iteration = 1, 1
        while current <= n:
            # Compute the total number of operations
            operations += (min(n, current * 4 - 1) - current + 1) * iteration
            current *= 4
            iteration += 1
        return operations