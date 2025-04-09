# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # Iterate the array
        seen = set([k])
        for num in nums:
            # Counting unique numbers
            seen.add(num)

            # If we find a number less than k, task is impossible
            if num < k:
                return -1
        
        # Otherwise, we iteratively reduce each unique number from the top
        return len(seen) - 1