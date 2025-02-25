# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        # Using prefix sum
        subarrays, prefix = 0, 0
        evens, odds = 1, 0

        # Iterate the array
        for num in arr:
            # And add to prefix sum
            prefix += num

            # If the current prefix sum is odd
            if prefix % 2:
                # We can add it to our even subarrays and get odds
                subarrays += evens
                odds += 1
            
            # If it is even
            else:
                # We can add it to our odd subarrays and get odds
                subarrays += odds
                evens += 1
        
        # Finally, return the subarrays modulo-ed
        return subarrays % int(1e9 + 7)

    