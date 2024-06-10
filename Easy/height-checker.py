# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # Using counting sort
        counts = [0] * 100

        # First iterate heights array, populating counts list
        for height in heights:
            counts[height-1] += 1
        
        # Then we can iterate frequencies of counts array,
        # noting down if we ever observe any discrepancies
        discrepancies = 0
        pointer = 0
        for i in range(100):
            while counts[i]:
                if heights[pointer]-1 != i:
                    discrepancies += 1
                counts[i] -= 1
                pointer += 1
        
        # Return total number of discrepancies
        return discrepancies