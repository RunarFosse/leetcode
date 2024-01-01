# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        front = 0
        for num in nums:
            if num == val:
                continue

            nums[front] = num
            front += 1
        
        return front

# Keep a pointer at the "front of the array", and move all nums not
# equal to val to this pointer.