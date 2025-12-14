# Author: Runar Fosse
# Time complexity: O(nlog m)
# Space complexity: O(1)

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        # Using binary search

        # Binary search the maximum number of candies
        left, right = 0, max(candies)
        while left < right:
            pivot = (left + right + 1) // 2

            # By checking the number of children we can give said number of candies
            current = k if not pivot else sum(candy // pivot for candy in candies)
            
            # And move bounds correspondingly
            if current >= k:
                left = pivot
            else:
                right = pivot - 1
        
        # Finally, return maximum amount of candies each child can get
        return left
