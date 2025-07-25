# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        # Iterate the array
        maximum, positives = -1e9, set()
        for num in nums:
            # Storing the maximum element
            maximum = max(num, maximum)
            if num > 0:
                # As well as every positive unique element
                positives.add(num)
        
        # If there exist positive elements in the array
        if maximum > 0:
            # Return the sum of them
            return sum(positives)
        
        # Otherwise, strictly return the maximum element
        return maximum
