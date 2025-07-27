# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        n = len(nums)

        # Keep count of the last and next other distinct element
        last = 0
        
        # Iterate the array
        count = 0
        for i in range(n - 1):
            # Skip if the same as last, and the same as the following element
            if nums[i] == nums[last] or nums[i] == nums[i + 1]:
                continue
            
            # Otherwise, check and count if hill or valley
            neighbours = (nums[last], nums[i + 1])
            if nums[i] > max(neighbours) or nums[i] < min(neighbours):
                count += 1
            
            # And update last element
            last = i
             
        # Finally, return the count of hills and valleys
        return count
