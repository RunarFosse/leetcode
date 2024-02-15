# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # Using greedy
        nums.sort()
        current, largest = 0, 0
        for i, num in enumerate(nums):
            if i > 1 and num < current:
                largest = current + num
            current += num
        
        return largest if largest else -1

# Iteratively sum numbers sorted in ascending order, if the current side is
# smaller than the sum of the previous sides, store current as the largest
# polygon perimiter (if sum consists of at least 3 sides).