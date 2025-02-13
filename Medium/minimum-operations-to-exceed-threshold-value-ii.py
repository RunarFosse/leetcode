# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(1)

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # First, turn the nums array into a heap
        heapify(nums)

        # Then perform operations
        operations = 0
        while len(nums) >= 2 and nums[0] < k:
            # Take the two smallest numbers
            x, y = heappop(nums), heappop(nums)

            # And add their new value back into the heap
            heappush(nums, x * 2 + y)

            # Increment operations count
            operations += 1
        
        # Return number of operations
        return operations

# We pop x of the heap before y. As the heap is a min-heap, it is guaranteed
# that x <= y. Thus, min(x, y) = x and max(x, y) = y. ;)