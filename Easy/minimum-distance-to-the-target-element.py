# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        # Using two pointer approach
        n = len(nums)

        # Iterate every element at a given distance
        distance = 0
        while start - distance >= 0 or start + distance < n:
            # Check whether either element is target
            left = start - distance >= 0 and nums[start - distance] == target
            right = start + distance < n and nums[start + distance] == target
            if left or right:
                return distance
            
            # If not, continue iterating
            distance += 1
        
        # If loop terminates, there does not exist any 'target' element in the array
        return n
