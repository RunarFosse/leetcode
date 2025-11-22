# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # Iterate the array
        operations = 0
        for num in nums:
            # Find the distance to a number divisible by three
            remainder = num % 3
            distance = min(remainder, 3 - remainder)

            # Finally, perform operations by closing that distance
            operations += distance
        
        # At last, return the minimum number of operations
        return operations
