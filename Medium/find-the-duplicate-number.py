# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Using slow/fast pointers
        slow, fast = 0, 0
        while not slow or slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow

# If we think of the input nums without duplicates as a DAG, 
# then a duplicate number would indicate a cycle. Therefore we can use
# a cycle finding algorithm to find this duplicate number.