# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        # Using sliding window
        n = len(nums)

        # First, sort the array in ascending order
        nums.sort()

        # Then slide a window
        maximum, start = 0, 0
        for end in range(n):
            # Ensure the window is a balanced subsequence
            while nums[end] > nums[start] * k:
                start += 1
            
            # And store the largest such balanced array
            maximum = max(end - start + 1, maximum)
        
        # Finally, return the number of removals needed for the maximum balanced array
        return n - maximum
