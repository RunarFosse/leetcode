# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Iterate nums, using values as indices.
        # We turn any number pointed to into floats.
        for i in range(n):
            pointer = int(nums[i]-1)
            if pointer >= 0 and pointer < n:
                nums[pointer] = float(nums[pointer])
        
        # Then iterate again, finding the first integer
        for i in range(n):
            if isinstance(nums[i], int):
                return i+1

        # If every number is a float, the next missing is
        # equal to the size of the list (+1 for indexing)
        return n+1