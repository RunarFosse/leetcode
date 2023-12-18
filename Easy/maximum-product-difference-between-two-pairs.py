# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        maxs, mins = (0, 0), (1e4, 1e4)
        for n in nums:
            if n > maxs[0]:
                maxs = (n, maxs[0])
            elif n > maxs[1]:
                maxs = (maxs[0], n)
            if n < mins[0]:
                mins = (n, mins[0])
            elif n < mins[1]:
                mins = (mins[0], n)
        
        return maxs[0] * maxs[1] - mins[0] * mins[1]
    
# This problem is obviously asking to find the 2 maximum and 2 minimum entries
# in the list, as obviously, the maximum product between two pairs has to be:
# maximum product between 2 entries - minimum product between 2 other entries.