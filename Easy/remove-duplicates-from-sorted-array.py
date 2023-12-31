# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        front = 0
        for num in nums:
            # Skip duplicates
            if num == nums[front]:
                continue

            # Add distincts to front of list
            nums[front+1] = num
            front += 1

        # Return the size of the new list
        return front + 1

# We modify nums in place by keeping one pointer, storing the position
# to place distinct numbers ("non-duplicates").