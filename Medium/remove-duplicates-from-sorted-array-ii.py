# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Using skip
        n = len(nums)
        i, skip = 2, 0
        while i+skip < n:
            # Check if current number appears more than twice
            if nums[i+skip] == nums[i-2]:
                # If so, skip one forward
                skip += 1
            # If not, add current number to insertion index and increment
            else:
                nums[i] = nums[i+skip]
                i += 1
        
        # Return the size of the remaining (non-removed) elements
        return n-skip

    
# Solved using a "skip"-count and insertion index,
# keeping track of how many indices we should skip over.

# Insertion index starts at 2, as we cannot possibly have an element appearing
# more than twice in the subarray nums[0:2] (consisting of 2 elements).