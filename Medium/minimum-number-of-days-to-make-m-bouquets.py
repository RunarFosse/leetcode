# Author: Runar Fosse
# Time complexity: O(nlog a)
# Space complexity: O(1)

# where a is the maximum element in the array

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        # Using binary search

        left, right = 0, max(bloomDay)
        while left <= right:
            d = ceil((left + right) / 2)

            # We greedily partition the array
            bouquets, current_size = 0, 0
            for day in bloomDay:
                current_size += 1
                if d < day:
                    current_size = 0
                if current_size == k:
                    bouquets += 1
                    current_size = 0
            
            # If left and right pointer are close, then binary
            # search has terminated so we return our result
            if left >= right-1:
                return d if bouquets >= m else -1
            
            # If not, move pointers 
            if bouquets < m:
                left = d
            else:
                right = d

# We use binary search to find the first possible day d where we can partition
# the array into m different k sized partitions, containing only elements
# less than or equal to d.