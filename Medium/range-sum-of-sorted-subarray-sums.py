# Author: Runar Fosse
# Time complexity: O(n^2log n)
# Space complexity: O(n)

class Solution:
    mod = int(1e9) + 7
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        # Using priority queue

        # First add all nums and corresponding index to priority queue
        queue = []
        for i in range(n):
            heappush(queue, (nums[i], i))

        # Then calculate sum of wanted range, starting from smallest value
        result, current = 0, 0
        for i in range(right):
            value, index = heappop(queue)

            # Check if we should we are within the range, if so add to sum
            if i+1 >= left:
                result = (result + value) % self.mod

            # If the current element is not the last in the array, 
            # add back into queue with the next element added
            if index < n-1:
                heappush(queue, (value + nums[index+1], index+1))
            
        # Return the final range sum
        return result