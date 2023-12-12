# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxes = (-1, -1)
        for n in nums:
            if n > maxes[0]:
                maxes = (n, maxes[0])
            elif n > maxes[1]:
                maxes = (maxes[0], n)
        
        return (maxes[0] - 1) * (maxes[1] - 1)
        

# As numbers cannot be negative, store the 2 largest numbers.