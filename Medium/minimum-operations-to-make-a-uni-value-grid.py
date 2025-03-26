# Author: Runar Fosse
# Time complexity: O(mnlog(mn))
# Space complexity: O(mn)

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # First, unroll the grid into a list
        numbers = [number for row in grid for number in row]

        # Then sort and find the median
        median = sorted(numbers)[len(numbers) // 2]
        
        # Then iterate them
        operations = 0
        for number in numbers:
            # If we cannot create the median, return early
            if abs(number - median) % x:
                return -1
            
            # Otherwise, add operations to make equal to median
            operations += abs(number - median) // x
        
        # Finally, return the minimum number of operations
        return operations