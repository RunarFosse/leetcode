# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # Insert number into rearranged list depending on sign
        rearranged = [0] * len(nums)
        positive, negative = 0, 1
        for num in nums:
            if num > 0:
                rearranged[positive] = num
                positive += 2
            else:
                rearranged[negative] = num
                negative += 2
        
        # Return the rearranged list
        return rearranged