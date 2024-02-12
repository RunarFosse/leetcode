# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majorityElement = None
        maxFrequency = 0

        # Step through the array
        for num in nums:
            # If maxFrequency is 0, override majority element
            if not maxFrequency:
                majorityElement = num
            
            # Add or subtract depending on current state of num with
            # respect to majority element
            maxFrequency += 1 if majorityElement == num else -1
        
        return majorityElement